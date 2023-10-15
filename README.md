# Data Analysis Bot 

- Project at [Autonomous Agents Hackathon@AGI House](https://partiful.com/e/YI5dqycxq2o87Dx2Bn2o) on October 24, 2023
- Sponsored by [Sebastian Thrun](http://robots.stanford.edu/personal.html) and [Brett Kuprel](https://www.linkedin.com/in/kuprel) from Sage AI and [Hendrik Dahlkamp](https://www.linkedin.com/in/hendrik-dahlkamp-12981) 


## Setup

Setup using Python 3.8, running
```
sh install.sh
```

Note that access to the ChatGPT/Claude API is needed.

## Run

Bot

```
python -u -m MLAgentBench.runner --python $(which python) --task spaceship-titanic --device 0 --log-dir first_test --work-dir workspace
```

Frontend
```
streamlit run frontend/home.py
```
