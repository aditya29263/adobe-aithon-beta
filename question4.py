import numpy as np
from predict import predict
object_ideal = predict("images/", show=True)
object_other = predict("images/", show=True)
similarity_score = calculate_similarity(object_ideal,object_other)
return similarity_score
