# agent-hack
10/24 hackathon on llm agents

python -u -m MLAgentBench.runner --python $(which python) --task cifar10 --device 0 --log-dir first_test  
--work-dir workspace --llm-name gpt-4 --edit-script-llm-name gpt-4 --fast-llm-name gpt-3.5-turbo
