# Copyright 2017 The UAI-SDK Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from uaitrain.api.base_op import BaseUAITrainAPIOp

class GetUAITrainTensorboardUrlOp(BaseUAITrainAPIOp):
    ACTION_NAME = "GetUAITrainTensorboardUrl"
    """
    GetUAITrainTensorboardUrlOp
        Compatable with UAI Train GetUAITrainTensorboardUrl API func
        Input:
            pub_key             string(required) Public key of the user
            priv_key            string(required) Private key of the user
            project_id          int(optional)    Project ID of the job
            region              string(optional) Which Region to run the job
            zone                string(optional) Which Zone in the Region to run the job
            PkgType         string(required) Package Type to check including OS, Python, AIFrame, Accelerator

        Output:
            RetCode       int(required)                Op return code: 0: success, others: error code
            Action        string(required)             Action name
            Message       string(not required)         Message: error description

    """

    def __init__(self, pub_key, priv_key, job_id, project_id="", region="", zone=""):
        super(GetUAITrainTensorboardUrlOp, self).__init__(self.ACTION_NAME,
                                                     pub_key,
                                                     priv_key,
                                                     project_id,
                                                     region,
                                                     zone)
        self.cmd_params["TrainJobId"] = job_id

    def _check_args(self):
        super(GetUAITrainTensorboardUrlOp, self)._check_args()

        if self.cmd_params["TrainJobId"] == "" or type(self.cmd_params["TrainJobId"]) != str:
            raise RuntimeError("job_id shoud be <str> and is not nil.")