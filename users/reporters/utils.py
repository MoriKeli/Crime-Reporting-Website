from django.core.exceptions import ValidationError
import magic

def validate_file_type(file):
    """ 
        This function is used to validate if an uploaded file is a supported file type. 
        The function validates if the user has uploaded a valid file.
        Accepted media file extensions/type are: .3gp, .gif, .jpeg, .jpg, .mp3, .mp4, .ogg
    """
    accept = [
        
    ]
    file_mime_type = magic.from_buffer(file.read(2048), mime=True)

    if file_mime_type not in accept:
        raise ValidationError('Unsupported file type!')