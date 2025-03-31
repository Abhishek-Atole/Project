#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>  // Include for std::string
#include <opencv2/opencv.hpp>
#include <iostream>

namespace py = pybind11;

py::array preprocess_image(const std::string& input_path) {
    std::cout << "Input path: " << input_path << std::endl;

    // Read the input image
    cv::Mat image = cv::imread(input_path, cv::IMREAD_COLOR);
    if (image.empty()) {
        throw std::runtime_error("Could not open or find the image: " + input_path);
    }

    // Convert to grayscale
    cv::Mat gray_image;
    cv::cvtColor(image, gray_image, cv::COLOR_BGR2GRAY);

    // Apply thresholding
    cv::Mat thresholded_image;
    cv::threshold(gray_image, thresholded_image, 128, 255, cv::THRESH_BINARY);

    // Create a py::capsule to manage the lifetime of the OpenCV matrix
    auto capsule = py::capsule(new cv::Mat(thresholded_image), [](void *v) {
        delete static_cast<cv::Mat *>(v);
    });

    // Create a py::array_t object from the OpenCV matrix
    return py::array_t<uint8_t>(
        {thresholded_image.rows, thresholded_image.cols},  // Shape
        {thresholded_image.step[0], thresholded_image.step[1]},  // Strides
        thresholded_image.data,  // Data pointer
        capsule  // Capsule to manage memory
    );
}

PYBIND11_MODULE(image_preprocessor, m) {
    m.def("preprocess_image", &preprocess_image, "Preprocess an image");
}