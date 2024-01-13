import bentoml
from bentoml.io import Text
from tensorflow.keras.preprocessing import image
import numpy as np

runner = bentoml.tensorflow.get("chest-cancer:latest").to_runner()

svc = bentoml.Service(
    name="chest-cancer", runners=[runner]
)

@svc.api(input=Text(), output=Text())
async def classifier(file_path):
    img = image.load_img(file_path, target_size = (224,224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)
    prediction =  await runner.async_run(img)
    prediction = np.argmax(prediction, axis=1)
    if prediction[0] == 1:
        result = 'Normal'
    else:
        result = 'Adenocarcinoma Cancer'
    return result