import tensorflow as tf


def process_images(model, image_paths, size, preprocess_input, top_k) -> list:
    result = []
    for idx, image_path in enumerate(image_paths):
        # Read the image using TensorFlow.
        tf_image = tf.io.read_file(image_path)
        # Decode the above `tf_image` from a Bytes string to a numeric Tensor.
        decoded_image = tf.image.decode_image(tf_image)

        # Resize the image to the spatial size required by the ml.
        image_resized = tf.image.resize(decoded_image, size)
        # Add a batch dimension to the first axis (required).
        image_batch = tf.expand_dims(image_resized, axis=0)
        # Pre-process the input image.
        image_batch = preprocess_input(image_batch)
        # Forward pass through the ml to make predictions.
        preds = model.predict(image_batch)
        # Decode (and rank the top-k) predictions.
        # Returns a list of tuples: (class ID, class description, probability)
        decoded_preds = tf.keras.applications.imagenet_utils.decode_predictions(
            preds=preds,
            top=5
        )

        if top_k > 5:
            top_k = 5
        prediction = []
        for jdx in range(top_k):
            subdict = {
                f"top": jdx + 1,
                f"description": decoded_preds[0][jdx][1],
                f"probability": "{:.2f}%".format(float(decoded_preds[0][jdx][2]) * 100)
            }
            prediction.append(subdict)
        d = {
            "image_number": idx + 1,
            "prediction": prediction
        }
        result.append(d)

    return result
