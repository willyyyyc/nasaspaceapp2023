from typing import TYPE_CHECKING
import numpy as np
import cv2
if TYPE_CHECKING:
    from Frame import Frame
    from numpy import ndarray


class Star:
    def __init__(self, region:'ndarray', frame: 'Frame') -> None:
        self.frame = frame
        self.intensity = None
        self.size = None
        self.colour = None
        self.region = region
        self.calculate_intensity_and_size()

    def calculate_intensity_and_size(self):
        if self.region is not None:
            # Convert the region to grayscale if needed
            if len(self.region.shape) == 3:
                region_gray = cv2.cvtColor(self.region, cv2.COLOR_BGR2GRAY)
            else:
                region_gray = self.region

            # Calculate intensity as the mean pixel value in the region
            self.intensity = np.mean(region_gray)

            # Calculate size as the number of pixels in the region
            self.size = region_gray.shape[0] * region_gray.shape[1]
    
    def __str__(self) -> str:
        return f"Star: intensity={self.intensity}, size={self.size}, colour={self.colour}"