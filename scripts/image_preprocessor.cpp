#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <opencv2/opencv.hpp>
#include <iostream>

namespace py = pybind11;

py::array preprocess_image(const std::string& input_path) {
    std::cout << "Input path: " << input_path << std::endl;

    // Read the input image
    cv::Mat image = cv::imread(input_path, cv::IMREAD_COLOR);
    if (image.empty()) {
        throw std::runtime_error("Could not open or find the image");
    }

    // Convert to grayscale
    cv::Mat gray_image;
    cv::cvtColor(image, gray_image, cv::COLOR_BGR2GRAY);

    // Apply thresholding
    cv::Mat thresholded_image;
    cv::threshold(gray_image, thresholded_image, 128, 255, cv::THRESH_BINARY);

    // Create a py::array_t object from the OpenCV matrix
    py::array_t<uint8_t> result({thresholded_image.rows, thresholded_image.cols}, thresholded_image.data);

    return result;
}

PYBIND11_MODULE(image_preprocessor, m) {
    m.def("preprocess_image", &preprocess_image, "Preprocess an image");
}