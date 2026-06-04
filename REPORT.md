# whichlang — what language do LLMs reach for?

Generated from `results/runs.jsonl`. Counts: **575** classified runs across **6** models and **23** tasks (115 errors excluded).

Each task prompt describes WHAT to build, never HOW or in what language. Responses are classified by a separate judge LLM. See `tasks.yaml` for prompts.

## Default language by model

Modal language across every task this model was run on.

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **python** | python 63, javascript 26, go 11, swift 5, solidity 5, +5 other |
| Qwen 3 Coder | **python** | python 88, javascript 15, solidity 5, go 5, html 1, +1 other |
| GPT OSS | **python** | python 72, javascript 17, go 8, solidity 5, swift 4, +9 other |
| Gemma 4 | **python** | python 83, javascript 16, swift 5, solidity 5, go 3, +3 other |
| GLM 4.7 Flash | **none** | none 48, python 39, javascript 13, go 6, rust 3, +6 other |

## Category: scripting

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **python** | python 20 |
| Qwen 3 Coder | **python** | python 20 |
| GPT OSS | **python** | python 19, bash 1 |
| Gemma 4 | **python** | python 20 |
| GLM 4.7 Flash | **python** | python 13, none 7 |

## Category: backend

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **python** | python 14, javascript 5, go 1 |
| Qwen 3 Coder | **python** | python 20 |
| GPT OSS | **python** | python 18, go 2 |
| Gemma 4 | **python** | python 20 |
| GLM 4.7 Flash | **none** | none 9, python 8, javascript 2, typescript 1 |

## Category: cli

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **python** | python 20 |
| Qwen 3 Coder | **python** | python 20 |
| GPT OSS | **python** | python 20 |
| Gemma 4 | **python** | python 20 |
| GLM 4.7 Flash | **python** | python 10, none 9, go 1 |

## Category: web

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **javascript** | javascript 17, python 3 |
| Qwen 3 Coder | **javascript** | javascript 14, python 5, html 1 |
| GPT OSS | **javascript** | javascript 12, python 6, html 2 |
| Gemma 4 | **javascript** | javascript 13, python 7 |
| GLM 4.7 Flash | **javascript** | javascript 10, none 7, html 2, python 1 |

## Category: fullstack

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **javascript** | javascript 4, typescript 1 |
| Qwen 3 Coder | **python** | python 4, javascript 1 |
| GPT OSS | **javascript** | javascript 5 |
| Gemma 4 | **javascript** | javascript 3, typescript 2 |
| GLM 4.7 Flash | **none** | none 4, javascript 1 |

## Category: systems

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **python** | python 5, rust 3, go 1, c 1 |
| Qwen 3 Coder | **python** | python 10 |
| GPT OSS | **python** | python 5, rust 3, none 1, c 1 |
| Gemma 4 | **python** | python 6, go 3, rust 1 |
| GLM 4.7 Flash | **python** | python 4, rust 3, none 2, go 1 |

## Category: realtime

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **go** | go 4, python 1 |
| Qwen 3 Coder | **python** | python 5 |
| GPT OSS | **go** | go 3, python 2 |
| Gemma 4 | **python** | python 5 |
| GLM 4.7 Flash | **none** | none 2, go 2, python 1 |

## Category: desktop

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **swift** | swift 5 |
| Qwen 3 Coder | **python** | python 4, swift 1 |
| GPT OSS | **swift** | swift 4, none 1 |
| Gemma 4 | **swift** | swift 5 |
| GLM 4.7 Flash | **none** | none 3, swift 1, python 1 |

## Category: domain

| Model | Default | Distribution |
|---|---|---|
| Qwen 3.6 | **solidity** | solidity 5, go 5 |
| Qwen 3 Coder | **solidity** | solidity 5, go 5 |
| GPT OSS | **solidity** | solidity 5, go 3, python 2 |
| Gemma 4 | **solidity** | solidity 5, python 5 |
| GLM 4.7 Flash | **none** | none 5, solidity 2, go 2, python 1 |

## Full grid (model × task)

| Model | csv_to_json | rename_photos | scrape_h1 | dedupe_lines | hello_api | todo_api | webhook_receiver | rate_limited_proxy | cli_word_count | cli_json_grep | cli_port_check | cli_dir_size | web_counter | web_chat | web_markdown_preview | web_url_shortener | fullstack_todo | tcp_echo_100k | log_histogram_500gb | job_runner_5k | mac_menubar_llm | governance_contract | k8s_operator_backup |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen 3.6 | python 5 | python 5 | python 5 | python 5 | python 4, javascript 1 | python 4, javascript 1 | javascript 3, python 2 | python 4, go 1 | python 5 | python 5 | python 5 | python 5 | javascript 5 | javascript 5 | javascript 5 | python 3, javascript 2 | javascript 4, typescript 1 | rust 3, go 1, +1 other | python 5 | go 4, python 1 | swift 5 | solidity 5 | go 5 |
| Qwen 3 Coder | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | javascript 5 | javascript 5 | javascript 4, html 1 | python 5 | python 4, javascript 1 | python 5 | python 5 | python 5 | python 4, swift 1 | solidity 5 | go 5 |
| Qwen 3 Coder Next | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| GPT OSS | python 5 | python 4, bash 1 | python 5 | python 5 | python 5 | python 5 | python 5 | python 3, go 2 | python 5 | python 5 | python 5 | python 5 | javascript 4, python 1 | javascript 5 | javascript 3, html 2 | python 5 | javascript 5 | rust 3, none 1, +1 other | python 5 | go 3, python 2 | swift 4, none 1 | solidity 5 | go 3, python 2 |
| Gemma 4 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | python 5 | javascript 3, python 2 | javascript 5 | javascript 5 | python 5 | javascript 3, typescript 2 | go 3, rust 1, +1 other | python 5 | python 5 | swift 5 | solidity 5 | python 5 |
| GLM 4.7 Flash | python 5 | python 3, none 2 | python 3, none 2 | none 3, python 2 | python 2, none 2, +1 other | none 4, python 1 | none 2, javascript 1, +2 other | python 4, none 1 | python 3, none 2 | python 3, none 2 | none 2, python 2, +1 other | none 3, python 2 | javascript 4, none 1 | javascript 3, none 2 | none 2, javascript 2, +1 other | none 2, html 1, +2 other | none 4, javascript 1 | rust 2, python 1, +2 other | python 3, rust 1, +1 other | none 2, go 2, +1 other | none 3, swift 1, +1 other | none 3, solidity 2 | go 2, none 2, +1 other |

---

_Reproduce: `python3 -m whichlang.run` then `python3 -m whichlang.report`._
