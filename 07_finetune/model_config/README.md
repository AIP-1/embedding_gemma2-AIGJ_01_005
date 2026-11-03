---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:282
- loss:MatryoshkaLoss
- loss:MultipleNegativesRankingLoss
base_model: google/embeddinggemma-2
widget:
- source_sentence: 지난달 경보 통계
  sentences:
  - 경보 기록은 1년간 보관해 월별 발생 횟수와 원인을 분석한다.
  - 경보 기록은 1년간 보관해 월별 발생 횟수와 원인을 분석한다.
  - 에이전트는 답변할 때 근거가 된 센서 값과 측정 시각을 함께 보여 준다.
- source_sentence: 질의응답 점수
  sentences:
  - 발표 평가는 내용 40%, 시연 40%, 질의응답 20%로 구성된다.
  - 발표 평가는 내용 40%, 시연 40%, 질의응답 20%로 구성된다.
  - 에어컨 설정을 1도 높이면 냉방 전력 사용량이 약 7% 줄어든다.
- source_sentence: 라돈 측정 주기
  sentences:
  - 라돈은 지하나 1층 공간에서 높게 나올 수 있어 연 1회 측정한다.
  - 에어컨 설정을 1도 높이면 냉방 전력 사용량이 약 7% 줄어든다.
  - 라돈은 지하나 1층 공간에서 높게 나올 수 있어 연 1회 측정한다.
- source_sentence: 문단속 담당
  sentences:
  - 난방 시 송풍 방향은 아래쪽으로 두어야 따뜻한 공기가 바닥부터 데운다.
  - 센서 고장 경보와 환경 경보는 담당자가 다르므로 분리해서 보낸다.
  - 강의실을 마지막으로 나가는 사람은 창문을 닫고 냉난방기와 조명을 끈다.
- source_sentence: 경보 중복 처리
  sentences:
  - 같은 경보가 10분 안에 반복되면 하나로 묶어 알림 피로를 줄인다.
  - 서비스는 systemd로 등록해 재부팅 후 자동으로 다시 시작되게 한다.
  - 에이전트의 모든 제어 명령은 시각·대상·이유와 함께 감사 로그에 남는다.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: SentenceTransformer based on google/embeddinggemma-2
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: classroom
      type: classroom
    metrics:
    - type: cosine_accuracy@1
      value: 0.9166666666666666
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.9666666666666667
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9666666666666667
      name: Cosine Accuracy@5
    - type: cosine_precision@1
      value: 0.9166666666666666
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.32222222222222213
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.19333333333333327
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09999999999999996
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.9166666666666666
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.9666666666666667
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.9666666666666667
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 1.0
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.9557224021297918
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.9416666666666668
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.9416666666666667
      name: Cosine Map@100
---

# SentenceTransformer based on google/embeddinggemma-2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [google/embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2) on the json dataset. It maps inputs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [google/embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2) <!-- at revision 914f7f89142e33e77833254d9c9b90c3cef7303b -->
- **Maximum Sequence Length:** 1000000000000000019884624838656 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modalities:** Text, Image, Audio, Video, Message
- **Training Dataset:**
    - json
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'image': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'audio': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'video': {'method': 'forward', 'method_output_name': 'last_hidden_state'}, 'message': {'method': 'forward', 'method_output_name': 'last_hidden_state', 'format': 'structured'}}, 'module_output_name': 'token_embeddings', 'architecture': 'EmbeddingGemma2Model'})
  (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({'module_input_name': 'sentence_embedding', 'module_output_name': 'sentence_embedding'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
queries = [
    '수업 중에 너무 졸려요 공기 때문인가요',
]
documents = [
    '강의실 CO2 농도가 1000ppm을 넘으면 졸음과 집중력 저하가 나타나므로 즉시 환기한다.',
    'CO2가 1500ppm을 넘으면 창문 개방과 기계 환기를 동시에 가동하는 2단계 환기를 실시한다.',
    '기계 환기 장치(전열교환기)는 실내 공기의 열을 일부 회수해 겨울에도 실내 온도 손실을 줄인다.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 768] [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[0.6696, 0.4880, 0.4061]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Information Retrieval

* Dataset: `classroom`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "query_prompt_name": "SearchQuery",
      "corpus_prompt_name": "Document"
  }
  ```

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.9167     |
| cosine_accuracy@3   | 0.9667     |
| cosine_accuracy@5   | 0.9667     |
| cosine_precision@1  | 0.9167     |
| cosine_precision@3  | 0.3222     |
| cosine_precision@5  | 0.1933     |
| cosine_precision@10 | 0.1        |
| cosine_recall@1     | 0.9167     |
| cosine_recall@3     | 0.9667     |
| cosine_recall@5     | 0.9667     |
| cosine_recall@10    | 1.0        |
| **cosine_ndcg@10**  | **0.9557** |
| cosine_mrr@10       | 0.9417     |
| cosine_map@100      | 0.9417     |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### json

* Dataset: json
* Size: 282 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 100 samples:
  |          | anchor                                                                            | positive                                                                          |
  |:---------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type     | string                                                                            | string                                                                            |
  | modality | text                                                                              | text                                                                              |
  | details  | <ul><li>min: 6 tokens</li><li>mean: 10.82 tokens</li><li>max: 16 tokens</li></ul> | <ul><li>min: 24 tokens</li><li>mean: 31.2 tokens</li><li>max: 43 tokens</li></ul> |
* Samples:
  | anchor                             | positive                                                         |
  |:-----------------------------------|:-----------------------------------------------------------------|
  | <code>수업 중에 너무 졸려요 공기 때문인가요</code> | <code>강의실 CO2 농도가 1000ppm을 넘으면 졸음과 집중력 저하가 나타나므로 즉시 환기한다.</code> |
  | <code>CO2 몇 ppm부터 환기해야 해요?</code>  | <code>강의실 CO2 농도가 1000ppm을 넘으면 졸음과 집중력 저하가 나타나므로 즉시 환기한다.</code> |
  | <code>이산화탄소 높으면 집중이 안 되나요</code>   | <code>강의실 CO2 농도가 1000ppm을 넘으면 졸음과 집중력 저하가 나타나므로 즉시 환기한다.</code> |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "MultipleNegativesRankingLoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `learning_rate`: 2e-05
- `warmup_steps`: 0.1
- `gradient_accumulation_steps`: 2
- `bf16`: True
- `prompts`: {'anchor': 'task: search result | query: ', 'positive': 'title: none | text: '}
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 8
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 2e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0.1
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 2
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1.0
- `label_smoothing_factor`: 0.0
- `bf16`: True
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 8
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: {'anchor': 'task: search result | query: ', 'positive': 'title: none | text: '}
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
| Epoch  | Step | Training Loss | classroom_cosine_ndcg@10 |
|:------:|:----:|:-------------:|:------------------------:|
| 0.5556 | 10   | 1.9923        | -                        |
| 1.0    | 18   | -             | 0.9557                   |
| 1.1111 | 20   | 1.4558        | -                        |
| 1.6667 | 30   | 0.7881        | -                        |
| 2.0    | 36   | -             | 0.9557                   |
| 2.2222 | 40   | 0.7165        | -                        |
| 2.7778 | 50   | 0.6213        | -                        |
| 3.0    | 54   | -             | 0.9557                   |


### Training Time
- **Training**: 3.6 minutes
- **Evaluation**: 1.7 seconds
- **Total**: 3.7 minutes

### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 6.2.0
- Transformers: 5.20.1
- PyTorch: 2.11.0+cu130
- Accelerate: 1.15.0
- Datasets: 5.1.0
- Tokenizers: 0.23.3

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MatryoshkaLoss
```bibtex
@misc{kusupati2024matryoshka,
    title={Matryoshka Representation Learning},
    author={Aditya Kusupati and Gantavya Bhatt and Aniket Rege and Matthew Wallingford and Aditya Sinha and Vivek Ramanujan and William Howard-Snyder and Kaifeng Chen and Sham Kakade and Prateek Jain and Ali Farhadi},
    year={2024},
    eprint={2205.13147},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->