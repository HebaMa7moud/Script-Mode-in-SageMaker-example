{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2022-08-08 15:48:34 Starting - Starting the training job...\n",
      "2022-08-08 15:48:57 Starting - Preparing the instances for trainingProfilerReport-1659973714: InProgress\n",
      ".........\n",
      "2022-08-08 15:50:30 Downloading - Downloading input data......\n",
      "2022-08-08 15:51:26 Training - Downloading the training image......\n",
      "2022-08-08 15:52:32 Uploading - Uploading generated training model\n",
      "2022-08-08 15:52:32 Failed - Training job failed\n",
      "\u001b[34mbash: cannot set terminal process group (-1): Inappropriate ioctl for device\u001b[0m\n",
      "\u001b[34mbash: no job control in this shell\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:18,644 sagemaker-training-toolkit INFO     Imported framework sagemaker_pytorch_container.training\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:18,648 sagemaker-training-toolkit INFO     No GPUs detected (normal if no gpus installed)\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:18,661 sagemaker_pytorch_container.training INFO     Block until all host DNS lookups succeed.\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:18,669 sagemaker_pytorch_container.training INFO     Invoking user training script.\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:19,236 sagemaker-training-toolkit INFO     No GPUs detected (normal if no gpus installed)\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:19,255 sagemaker-training-toolkit INFO     No GPUs detected (normal if no gpus installed)\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:19,274 sagemaker-training-toolkit INFO     No GPUs detected (normal if no gpus installed)\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:19,290 sagemaker-training-toolkit INFO     Invoking user script\u001b[0m\n",
      "\u001b[34mTraining Env:\u001b[0m\n",
      "\u001b[34m{\n",
      "    \"additional_framework_parameters\": {},\n",
      "    \"channel_input_dirs\": {},\n",
      "    \"current_host\": \"algo-1\",\n",
      "    \"framework_module\": \"sagemaker_pytorch_container.training:main\",\n",
      "    \"hosts\": [\n",
      "        \"algo-1\"\n",
      "    ],\n",
      "    \"hyperparameters\": {\n",
      "        \"batch-size\": \"32\",\n",
      "        \"epochs\": \"2\",\n",
      "        \"lr\": \"0.001\",\n",
      "        \"test-batch-size\": \"100\"\n",
      "    },\n",
      "    \"input_config_dir\": \"/opt/ml/input/config\",\n",
      "    \"input_data_config\": {},\n",
      "    \"input_dir\": \"/opt/ml/input\",\n",
      "    \"is_master\": true,\n",
      "    \"job_name\": \"sagemaker-script-mode-2022-08-08-15-48-34-400\",\n",
      "    \"log_level\": 20,\n",
      "    \"master_hostname\": \"algo-1\",\n",
      "    \"model_dir\": \"/opt/ml/model\",\n",
      "    \"module_dir\": \"s3://sagemaker-us-east-1-324910130953/sagemaker-script-mode-2022-08-08-15-48-34-400/source/sourcedir.tar.gz\",\n",
      "    \"module_name\": \"pytorch_cifar\",\n",
      "    \"network_interface_name\": \"eth0\",\n",
      "    \"num_cpus\": 2,\n",
      "    \"num_gpus\": 0,\n",
      "    \"output_data_dir\": \"/opt/ml/output/data\",\n",
      "    \"output_dir\": \"/opt/ml/output\",\n",
      "    \"output_intermediate_dir\": \"/opt/ml/output/intermediate\",\n",
      "    \"resource_config\": {\n",
      "        \"current_host\": \"algo-1\",\n",
      "        \"current_instance_type\": \"ml.m5.large\",\n",
      "        \"current_group_name\": \"homogeneousCluster\",\n",
      "        \"hosts\": [\n",
      "            \"algo-1\"\n",
      "        ],\n",
      "        \"instance_groups\": [\n",
      "            {\n",
      "                \"instance_group_name\": \"homogeneousCluster\",\n",
      "                \"instance_type\": \"ml.m5.large\",\n",
      "                \"hosts\": [\n",
      "                    \"algo-1\"\n",
      "                ]\n",
      "            }\n",
      "        ],\n",
      "        \"network_interface_name\": \"eth0\"\n",
      "    },\n",
      "    \"user_entry_point\": \"pytorch_cifar.py\"\u001b[0m\n",
      "\u001b[34m}\u001b[0m\n",
      "\u001b[34mEnvironment variables:\u001b[0m\n",
      "\u001b[34mSM_HOSTS=[\"algo-1\"]\u001b[0m\n",
      "\u001b[34mSM_NETWORK_INTERFACE_NAME=eth0\u001b[0m\n",
      "\u001b[34mSM_HPS={\"batch-size\":\"32\",\"epochs\":\"2\",\"lr\":\"0.001\",\"test-batch-size\":\"100\"}\u001b[0m\n",
      "\u001b[34mSM_USER_ENTRY_POINT=pytorch_cifar.py\u001b[0m\n",
      "\u001b[34mSM_FRAMEWORK_PARAMS={}\u001b[0m\n",
      "\u001b[34mSM_RESOURCE_CONFIG={\"current_group_name\":\"homogeneousCluster\",\"current_host\":\"algo-1\",\"current_instance_type\":\"ml.m5.large\",\"hosts\":[\"algo-1\"],\"instance_groups\":[{\"hosts\":[\"algo-1\"],\"instance_group_name\":\"homogeneousCluster\",\"instance_type\":\"ml.m5.large\"}],\"network_interface_name\":\"eth0\"}\u001b[0m\n",
      "\u001b[34mSM_INPUT_DATA_CONFIG={}\u001b[0m\n",
      "\u001b[34mSM_OUTPUT_DATA_DIR=/opt/ml/output/data\u001b[0m\n",
      "\u001b[34mSM_CHANNELS=[]\u001b[0m\n",
      "\u001b[34mSM_CURRENT_HOST=algo-1\u001b[0m\n",
      "\u001b[34mSM_MODULE_NAME=pytorch_cifar\u001b[0m\n",
      "\u001b[34mSM_LOG_LEVEL=20\u001b[0m\n",
      "\u001b[34mSM_FRAMEWORK_MODULE=sagemaker_pytorch_container.training:main\u001b[0m\n",
      "\u001b[34mSM_INPUT_DIR=/opt/ml/input\u001b[0m\n",
      "\u001b[34mSM_INPUT_CONFIG_DIR=/opt/ml/input/config\u001b[0m\n",
      "\u001b[34mSM_OUTPUT_DIR=/opt/ml/output\u001b[0m\n",
      "\u001b[34mSM_NUM_CPUS=2\u001b[0m\n",
      "\u001b[34mSM_NUM_GPUS=0\u001b[0m\n",
      "\u001b[34mSM_MODEL_DIR=/opt/ml/model\u001b[0m\n",
      "\u001b[34mSM_MODULE_DIR=s3://sagemaker-us-east-1-324910130953/sagemaker-script-mode-2022-08-08-15-48-34-400/source/sourcedir.tar.gz\u001b[0m\n",
      "\u001b[34mSM_TRAINING_ENV={\"additional_framework_parameters\":{},\"channel_input_dirs\":{},\"current_host\":\"algo-1\",\"framework_module\":\"sagemaker_pytorch_container.training:main\",\"hosts\":[\"algo-1\"],\"hyperparameters\":{\"batch-size\":\"32\",\"epochs\":\"2\",\"lr\":\"0.001\",\"test-batch-size\":\"100\"},\"input_config_dir\":\"/opt/ml/input/config\",\"input_data_config\":{},\"input_dir\":\"/opt/ml/input\",\"is_master\":true,\"job_name\":\"sagemaker-script-mode-2022-08-08-15-48-34-400\",\"log_level\":20,\"master_hostname\":\"algo-1\",\"model_dir\":\"/opt/ml/model\",\"module_dir\":\"s3://sagemaker-us-east-1-324910130953/sagemaker-script-mode-2022-08-08-15-48-34-400/source/sourcedir.tar.gz\",\"module_name\":\"pytorch_cifar\",\"network_interface_name\":\"eth0\",\"num_cpus\":2,\"num_gpus\":0,\"output_data_dir\":\"/opt/ml/output/data\",\"output_dir\":\"/opt/ml/output\",\"output_intermediate_dir\":\"/opt/ml/output/intermediate\",\"resource_config\":{\"current_group_name\":\"homogeneousCluster\",\"current_host\":\"algo-1\",\"current_instance_type\":\"ml.m5.large\",\"hosts\":[\"algo-1\"],\"instance_groups\":[{\"hosts\":[\"algo-1\"],\"instance_group_name\":\"homogeneousCluster\",\"instance_type\":\"ml.m5.large\"}],\"network_interface_name\":\"eth0\"},\"user_entry_point\":\"pytorch_cifar.py\"}\u001b[0m\n",
      "\u001b[34mSM_USER_ARGS=[\"--batch-size\",\"32\",\"--epochs\",\"2\",\"--lr\",\"0.001\",\"--test-batch-size\",\"100\"]\u001b[0m\n",
      "\u001b[34mSM_OUTPUT_INTERMEDIATE_DIR=/opt/ml/output/intermediate\u001b[0m\n",
      "\u001b[34mSM_HP_BATCH-SIZE=32\u001b[0m\n",
      "\u001b[34mSM_HP_EPOCHS=2\u001b[0m\n",
      "\u001b[34mSM_HP_LR=0.001\u001b[0m\n",
      "\u001b[34mSM_HP_TEST-BATCH-SIZE=100\u001b[0m\n",
      "\u001b[34mPYTHONPATH=/opt/ml/code:/opt/conda/bin:/opt/conda/lib/python36.zip:/opt/conda/lib/python3.6:/opt/conda/lib/python3.6/lib-dynload:/opt/conda/lib/python3.6/site-packages\u001b[0m\n",
      "\u001b[34mInvoking script with the following command:\u001b[0m\n",
      "\u001b[34m/opt/conda/bin/python3.6 pytorch_cifar.py --batch-size 32 --epochs 2 --lr 0.001 --test-batch-size 100\u001b[0m\n",
      "\u001b[34mTraceback (most recent call last):\n",
      "  File \"pytorch_cifar.py\", line 149, in <module>\n",
      "    \"execution_count\": null,\u001b[0m\n",
      "\u001b[34mNameError: name 'null' is not defined\u001b[0m\n",
      "\u001b[34m2022-08-08 15:52:19,337 sagemaker-training-toolkit ERROR    ExecuteUserScriptError:\u001b[0m\n",
      "\u001b[34mCommand \"/opt/conda/bin/python3.6 pytorch_cifar.py --batch-size 32 --epochs 2 --lr 0.001 --test-batch-size 100\"\u001b[0m\n",
      "\u001b[34mTraceback (most recent call last):\n",
      "  File \"pytorch_cifar.py\", line 149, in <module>\n",
      "    \"execution_count\": null,\u001b[0m\n",
      "\u001b[34mNameError: name 'null' is not defined\u001b[0m\n"
     ]
    },
    {
     "ename": "UnexpectedStatusException",
     "evalue": "Error for Training job sagemaker-script-mode-2022-08-08-15-48-34-400: Failed. Reason: AlgorithmError: ExecuteUserScriptError:\nCommand \"/opt/conda/bin/python3.6 pytorch_cifar.py --batch-size 32 --epochs 2 --lr 0.001 --test-batch-size 100\"\nTraceback (most recent call last):\n  File \"pytorch_cifar.py\", line 149, in <module>\n    \"execution_count\": null,\nNameError: name 'null' is not defined, exit code: 1",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mUnexpectedStatusException\u001b[0m                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-f58ac9ef3076>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     15\u001b[0m )\n\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 17\u001b[0;31m \u001b[0mestimator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mwait\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/sagemaker/workflow/pipeline_context.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    207\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself_instance\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msagemaker_session\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcontext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    208\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 209\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mrun_func\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    210\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    211\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/sagemaker/estimator.py\u001b[0m in \u001b[0;36mfit\u001b[0;34m(self, inputs, wait, logs, job_name, experiment_config)\u001b[0m\n\u001b[1;32m   1004\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjobs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlatest_training_job\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1005\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mwait\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1006\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlatest_training_job\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwait\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlogs\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlogs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1007\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1008\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_compilation_job_name\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/sagemaker/estimator.py\u001b[0m in \u001b[0;36mwait\u001b[0;34m(self, logs)\u001b[0m\n\u001b[1;32m   2080\u001b[0m         \u001b[0;31m# If logs are requested, call logs_for_jobs.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2081\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mlogs\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;34m\"None\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2082\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msagemaker_session\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogs_for_job\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjob_name\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwait\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlog_type\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlogs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2083\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2084\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msagemaker_session\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwait_for_job\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjob_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/sagemaker/session.py\u001b[0m in \u001b[0;36mlogs_for_job\u001b[0;34m(self, job_name, wait, poll, log_type)\u001b[0m\n\u001b[1;32m   3849\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3850\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mwait\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3851\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_check_job_status\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mjob_name\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdescription\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"TrainingJobStatus\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3852\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mdot\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3853\u001b[0m                 \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/sagemaker/session.py\u001b[0m in \u001b[0;36m_check_job_status\u001b[0;34m(self, job, desc, status_key_name)\u001b[0m\n\u001b[1;32m   3390\u001b[0m                 \u001b[0mmessage\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3391\u001b[0m                 \u001b[0mallowed_statuses\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"Completed\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Stopped\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3392\u001b[0;31m                 \u001b[0mactual_status\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstatus\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3393\u001b[0m             )\n\u001b[1;32m   3394\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mUnexpectedStatusException\u001b[0m: Error for Training job sagemaker-script-mode-2022-08-08-15-48-34-400: Failed. Reason: AlgorithmError: ExecuteUserScriptError:\nCommand \"/opt/conda/bin/python3.6 pytorch_cifar.py --batch-size 32 --epochs 2 --lr 0.001 --test-batch-size 100\"\nTraceback (most recent call last):\n  File \"pytorch_cifar.py\", line 149, in <module>\n    \"execution_count\": null,\nNameError: name 'null' is not defined, exit code: 1"
     ]
    }
   ],
   "source": [
    "from sagemaker.pytorch import PyTorch\n",
    "from sagemaker import get_execution_role\n",
    "\n",
    "hyperparameters =  {\"batch-size\": \"32\", \"test-batch-size\": \"100\",\"epochs\": \"2\", \"lr\": \"0.001\"}\n",
    "\n",
    "estimator = PyTorch(\n",
    "    entry_point=\"pytorch_cifar.py\",\n",
    "    base_job_name=\"sagemaker-script-mode\",\n",
    "    role=get_execution_role(),\n",
    "    instance_count=1,\n",
    "    instance_type=\"ml.m5.large\",\n",
    "    hyperparameters=hyperparameters,\n",
    "    framework_version=\"1.8\",\n",
    "    py_version=\"py36\",\n",
    ")\n",
    "\n",
    "estimator.fit(wait=True)                 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (Data Science)",
   "language": "python",
   "name": "python3__SAGEMAKER_INTERNAL__arn:aws:sagemaker:us-east-1:081325390199:image/datascience-1.0"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}