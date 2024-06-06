from funasr import AutoModel

model = AutoModel(model="./Voice_translation", model_revision="v2.0.4",
                  vad_model="./Endpoint_detection", vad_model_revision="v2.0.4",
                  punc_model="./Ct_punc", punc_model_revision="v2.0.4",
                  )
res = model.generate(input=f"./datasets/bnb.m4a", 
            batch_size_s=300, 
            hotword='test')
print(res)