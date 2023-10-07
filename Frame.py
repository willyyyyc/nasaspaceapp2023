import cv2

from Star import Star

class Frame:
    def __init__(self, frame):
        self.frame = frame
        self._is_grayscale = False

    def get_grayscale(self) -> 'Frame':
        grayscale_frame = Frame(cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY))
        grayscale_frame._is_grayscale = True
        return grayscale_frame
    
    def get_blurry(self) -> 'Frame':
        blurred_frame = Frame(cv2.GaussianBlur(self.frame, (5, 5), 0))
        blurred_frame._is_grayscale = self._is_grayscale
        return blurred_frame

    def get_height(self):
        return self.frame.shape[0]

    def get_width(self):
        return self.frame.shape[1]

    def threshold(self, threshold_value, max_value=255, threshold_type=cv2.THRESH_BINARY) -> 'Frame':
        if self._is_grayscale:
            gray_frame = self.frame
        else:
            gray_frame = self.get_grayscale()

        _, thresholded_frame = cv2.threshold(gray_frame, threshold_value, max_value, threshold_type)
        return_frame =Frame(thresholded_frame)
        return_frame._is_grayscale = True
        return return_frame

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

    def find_high_intensity_regions(self, threshold_value=128):
        # Threshold the image to create a binary mask
        _, binary_mask = cv2.threshold(self.frame, threshold_value, 255, cv2.THRESH_BINARY)

        # Find contours in the binary mask
        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create an image to draw the contours on (a copy of the original frame)
        contour_image = self.frame.copy()

        # Draw the contours on the image (you can choose a different color and thickness)
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 1)

        # Create a list to store the extracted high-intensity regions
        high_intensity_regions = []

        # Iterate through the contours and extract the regions from the original frame
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            region = self.frame[y:y+h, x:x+w]
            high_intensity_regions.append(Star(region, self))

        return Frame(contour_image), high_intensity_regions

    def save(self, filename):
        cv2.imwrite(filename, self.frame)

    def display(self, window_name='Frame'):
        cv2.imshow(window_name, self.frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()