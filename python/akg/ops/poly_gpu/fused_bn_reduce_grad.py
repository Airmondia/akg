# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions andg
# limitations under the License.

"""fused_bn_reduce_grad"""
from __future__ import absolute_import
import akg
from akg.topi.cuda.injective_single_kernel import schedule_injective
from akg.ops.fused_gpu.fused_bn_reduce_grad import fused_bn_reduce_grad

@akg.schedule(schedule_injective)
def fused_bn_reduce_grad_manual(data0, data1, data2, data3, data4, data5, data6, data7, layout="NHWC", out_dtype="float16"):
    """Fused operater: fused_bn_reduce_grad, with manual schedule"""
    return fused_bn_reduce_grad(data0, data1, data2, data3, data4, data5, data6, data7,
                                                           layout, out_dtype)

def fused_bn_reduce_grad_auto(data0, data1, data2, data3, data4, data5, data6, data7, layout="NHWC", out_dtype="float16"):
    """Fused operater: fused_bn_reduce_grad, with auto schedule"""
    return fused_bn_reduce_grad(data0, data1, data2, data3, data4, data5, data6, data7,
                                                           layout, out_dtype)
