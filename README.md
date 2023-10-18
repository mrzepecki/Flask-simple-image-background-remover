# Flask simple image background remover

This Python application utilizes Flask and the rembg library to remove backgrounds from images. Users can submit images to the server, triggering the background removal process, and receive the processed images with transparent backgrounds. This user-friendly API-based solution simplifies the creation of images with transparent backgrounds, suitable for a variety of applications, from graphic design to e-commerce.

### Allowed HTTPs requests

#### POST `/v1/remove-background`

##### REQUEST

`FormData` with attached `file`

##### RESPONSE

`file` with `mimetype='image/png'`
