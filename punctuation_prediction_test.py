from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

inference_pipline = pipeline(
    task=Tasks.punctuation,
    model='./Ct_punc',
    model_revision="v2.0.4")

rec_result = inference_pipline(input='./datasets/punc_example.txt')
print(rec_result)