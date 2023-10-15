# UDABI: Unstructured Data Analysis and Business Intelligence

- Project at [Autonomous Agents Hackathon@AGI House](https://partiful.com/e/YI5dqycxq2o87Dx2Bn2o) on October 24, 2023
- Sponsored by [Sebastian Thrun](http://robots.stanford.edu/personal.html) and [Brett Kuprel](https://www.linkedin.com/in/kuprel) from Sage AI and [Hendrik Dahlkamp](https://www.linkedin.com/in/hendrik-dahlkamp-12981) 


UDABI is not just a chatbot; it's your data-driven ally in the world of business. With the power to transform unstructured data like CSV files, text, and more into invaluable business insights, UDABI revolutionizes the way you understand and leverage your data.


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

## Team

- [Rachel Freedman](https://rachelfreedman.github.io/)
- [Alexander Naumann](https://a-nau.github.io)
- [Alex Vessel](https://www.linkedin.com/in/alex-vesel-a315b11b6)
- [Jian Vora](https://jianvora.github.io/)

