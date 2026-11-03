import sys, numpy as np, cv2
sys.path.insert(0, sys.argv[1])
import calib_board as B
K0=np.array([[818.,0,424],[0,827,235],[0,0,1]]); K1=np.array([[680.6,0,319.5],[0,680.6,239.5],[0,0,1]]); D=np.zeros(5)
obj=B.board_points(9,6,0.024)
rng=np.random.default_rng(1)
def look(C,target,roll=0):
    f=target-C; f/=np.linalg.norm(f); up=np.array([0,0,1.]); r=np.cross(f,up); r/=np.linalg.norm(r); d=np.cross(f,r)
    R=np.stack([r,d,f]); c,s=np.cos(roll),np.sin(roll); return np.array([[c,-s,0],[s,c,0],[0,0,1]])@R
for flat,zb,noise,rev in [(False,1.0,0,False),(False,1.0,0.3,False),(True,0.72,0.3,False),(False,1.0,0,True),(False,1.0,0.3,True)]:
    # 진짜 방 좌표: 체커보드 중심 (0,0,zb), 카메라는 뒤쪽 -x
    C0=np.array([-1.5,0.25,1.25]); C1=np.array([-1.5,-0.25,1.25])
    Rw0=look(C0,np.array([0,0.1,zb]),np.radians(15)); Rw1=look(C1,np.array([0,-0.1,zb]))
    if flat: Xw=np.c_[obj[:,0],obj[:,1],zb+obj[:,2]]
    else:    Xw=np.c_[-obj[:,2],-obj[:,0],zb+obj[:,1]]   # 앞면이 카메라(-x) 쪽, 세로 = z
    def proj(R,C,K):
        t=(-R@C).reshape(3,1); p,_=cv2.projectPoints(Xw,cv2.Rodrigues(R)[0],t,K,D); return p.reshape(-1,2)+rng.normal(0,noise,(54,2)) if noise else p.reshape(-1,2)
    imgs=[proj(Rw0,C0,K0),proj(Rw1,C1,K1)[::-1]]    # cam1은 일부러 순서를 뒤집음
    if rev: imgs[0]=imgs[0][::-1]
    res=B.solve(obj,imgs,[K0,K1],[D,D],flat,zb)
    print("flat" if flat else "upright","noise",noise,"cam0 순서 뒤집음" if rev else "")
    for n,(R,t,e) in enumerate(res):
        print(" cam",n,(-R.T@t).ravel().round(3).tolist(),"reproj",round(e,3),"axis",(R.T@[0,0,1]).round(2).tolist())
    # 알려진 사람 어깨 점을 두 카메라로 삼각측량
    cam=lambda R,t,K:{"K":K,"dist":D,"R":R,"t":t,"P":K@np.hstack([R,t]),"C":(-R.T@t).ravel(),"Kinv":np.linalg.inv(K)}
    c0,c1=cam(res[0][0],res[0][1],K0),cam(res[1][0],res[1][1],K1)
    print(" 간격",round(float(np.linalg.norm(c0["C"]-c1["C"])),3))
