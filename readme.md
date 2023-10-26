# Installation

After cloning this repo, please install the dependencies using

`pip3 install -r requirements-asr`

Then, please download the model, as it was too large to be commited:

`wget elexunix.com/asr-project-model.pth -O default_test_model/model_best.pth`

# Usage

Then you can simply run
`train.py`
to train a new model based on my best config,

or
`test.py`
to test my best model on the standard test-clean which will produce a similar to output.json output file, the metrics will be in the very end:
just use `tail -n 20 output.json` to see them.

# sha256sum of the model

It is here before the deadline so you can make sure the model file was not modified after the deadline. After downloading the model, please verify the sha256sum:
`$ sha256sum default_test_model/model_best.pth`
`5cbeddba3fafb408c00b6d233116fe68e838be79e5f07fde73b9b0b29c6eecde  default_test_model/model_best.pth`
