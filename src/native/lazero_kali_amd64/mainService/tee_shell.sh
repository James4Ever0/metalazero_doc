#tee -a inputs.log | bash | tee -a outputs.log
tee -a inputs.log | bash 2>&1 | tee -a outputs.log
