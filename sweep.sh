python_script="your_python_script.py"

# Number of times to run the Python script
num_runs=1

# Loop to run the Python script multiple times
for ((i=1; i<=$num_runs; i++))
do
    log_file="logs_$i"
    workspace="workspace_$i"
    echo "Running Python process $i"
    python -u -m MLAgentBench.runner --python $(which python) --task covid_data --device 0 --log-dir $log_file --work-dir $workspace &
done
wait