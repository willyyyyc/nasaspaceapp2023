import cv2

class Frame:
    def __init__(self, frame):
        self.frame = frame

    def get_grayscale(self) -> 'Frame':
        return Frame(cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY))

    def get_height(self):
        return self.frame.shape[0]

    def get_width(self):
        return self.frame.shape[1]

    def threshold(self, threshold_value, max_value=255, threshold_type=cv2.THRESH_BINARY) -> 'Frame':
        gray_frame = self.get_grayscale()
        _, thresholded_frame = cv2.threshold(gray_frame, threshold_value, max_value, threshold_type)
        return Frame(thresholded_frame)

    def resize(self, width=None, height=None):
        if width is None and height is None:
            return self  # No need to resize

        if width is None:
            aspect_ratio = height / self.get_height()
            width = int(self.get_width() * aspect_ratio)
        elif height is None:
            aspect_ratio = width / self.get_width()
            height = int(self.get_height() * aspect_ratio)

        resized_frame = cv2.resize(self.frame, (width, height))
        return Frame(resized_frame)

    def save(self, filename):
        cv2.imwrite(filename, self.frame)

    def display(self, window_name='Frame'):
        cv2.imshow(window_name, self.frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()