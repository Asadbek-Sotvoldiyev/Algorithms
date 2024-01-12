def insertion_sort(arr):
    length = len(arr)
    count = 0
    for i in range(1,length):
        while arr[i]<arr[i-1] and i>0:
            count+=1
            arr[i],arr[i-1] = arr[i-1], arr[i]
            i-=1
    return count

def bubble_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            count+=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count

arr1 = [156, 428, 200, 211, 199, 325, 203, 436, 174, 35, 9, 199, 226, 413, 497, 214, 164, 352, 261, 434, 459, 323, 378, 162, 105, 67, 442, 152, 394, 216, 361, 109, 384, 251, 451, 216, 381, 288, 325, 371, 167, 39, 498, 150, 335, 415, 165, 101, 420, 447, 37, 426, 41, 170, 480, 250, 98, 139, 297, 240, 0, 442, 156, 291, 321, 75, 91, 38, 207, 225, 418, 217, 63, 113, 58, 434, 336, 23, 385, 235, 93, 329, 471, 216, 136, 427, 373, 461, 313, 354, 485, 271, 48, 273, 155, 65, 338, 2, 224, 372, 437, 145, 494, 67, 133, 171, 279, 62, 14, 200, 164, 401, 495, 344, 311, 53, 432, 458, 230, 282, 160, 69, 198, 314, 103, 27, 296, 383, 353, 420, 47, 155, 454, 365, 201, 99, 173, 272, 416, 301, 75, 415, 389, 436, 337, 45, 165, 233, 105, 96, 217, 110, 127, 415, 20, 186, 2, 358, 150, 441, 168, 210, 429, 136, 355, 492, 386, 200, 480, 394, 348, 177, 496, 377, 128, 77, 268, 193, 413, 339, 338, 361, 383, 168, 178, 341, 244, 328, 416, 128, 81, 376, 255, 422, 106, 347, 172, 394, 308, 306, 383, 383, 373, 406, 353, 0, 482, 129, 181, 92, 136, 482, 410, 441, 365, 84, 199, 197, 11, 346, 388, 42, 66, 465, 272, 213, 212, 95, 215, 323, 25, 9, 274, 96, 172, 404, 300, 60, 255, 446, 171, 174, 309, 258, 125, 401, 85, 289, 222, 226, 190, 160, 437, 6, 118, 113, 162, 450, 81, 307, 116, 80, 208, 276, 415, 304, 118, 358, 82, 34, 400, 316, 300, 168, 168, 117, 475, 62, 396, 423, 479, 69, 208, 88, 447, 371, 196, 389, 241, 486, 459, 423, 413, 373, 203, 77, 320, 299, 273, 450, 371, 432, 325, 237, 161, 137, 151, 111, 57, 171, 339, 285, 319, 404, 373, 173, 384, 270, 285, 359, 395, 121, 373, 189, 489, 132, 454, 396, 96, 429, 452, 432, 248, 211, 189, 477, 128, 296, 379, 219, 155, 379, 163, 401, 91, 211, 388, 364, 183, 68, 59, 416, 253, 404, 169, 16, 412, 352, 96, 495, 499, 34, 465, 97, 373, 195, 331, 28, 257, 169, 477, 326, 376, 32, 198, 67, 395, 169, 15, 360, 356, 42, 254, 157, 326, 462, 42, 154, 477, 126, 401, 77, 345, 295, 179, 109, 408, 154, 99, 125, 214, 70, 93, 16, 172, 148, 158, 149, 338, 344, 276, 213, 484, 89, 170, 110, 178, 413, 484, 335, 156, 420, 434, 97, 425, 101, 60, 60, 366, 289, 477, 261, 413, 293, 169, 313, 359, 202, 414, 445, 455, 363, 230, 328, 1, 229, 129, 21, 498, 248, 251, 105, 72, 66, 380, 82, 433, 224, 4, 437, 436, 327, 255, 403, 172, 117, 305, 203, 319, 474, 93, 331, 69, 463, 419, 26, 229, 457, 412, 58, 193, 67, 358, 292, 107, 5, 291, 416, 293, 6, 73, 242, 182, 101, 141, 194, 265, 91, 56, 250]
arr2 = [156, 428, 200, 211, 199, 325, 203, 436, 174, 35, 9, 199, 226, 413, 497, 214, 164, 352, 261, 434, 459, 323, 378, 162, 105, 67, 442, 152, 394, 216, 361, 109, 384, 251, 451, 216, 381, 288, 325, 371, 167, 39, 498, 150, 335, 415, 165, 101, 420, 447, 37, 426, 41, 170, 480, 250, 98, 139, 297, 240, 0, 442, 156, 291, 321, 75, 91, 38, 207, 225, 418, 217, 63, 113, 58, 434, 336, 23, 385, 235, 93, 329, 471, 216, 136, 427, 373, 461, 313, 354, 485, 271, 48, 273, 155, 65, 338, 2, 224, 372, 437, 145, 494, 67, 133, 171, 279, 62, 14, 200, 164, 401, 495, 344, 311, 53, 432, 458, 230, 282, 160, 69, 198, 314, 103, 27, 296, 383, 353, 420, 47, 155, 454, 365, 201, 99, 173, 272, 416, 301, 75, 415, 389, 436, 337, 45, 165, 233, 105, 96, 217, 110, 127, 415, 20, 186, 2, 358, 150, 441, 168, 210, 429, 136, 355, 492, 386, 200, 480, 394, 348, 177, 496, 377, 128, 77, 268, 193, 413, 339, 338, 361, 383, 168, 178, 341, 244, 328, 416, 128, 81, 376, 255, 422, 106, 347, 172, 394, 308, 306, 383, 383, 373, 406, 353, 0, 482, 129, 181, 92, 136, 482, 410, 441, 365, 84, 199, 197, 11, 346, 388, 42, 66, 465, 272, 213, 212, 95, 215, 323, 25, 9, 274, 96, 172, 404, 300, 60, 255, 446, 171, 174, 309, 258, 125, 401, 85, 289, 222, 226, 190, 160, 437, 6, 118, 113, 162, 450, 81, 307, 116, 80, 208, 276, 415, 304, 118, 358, 82, 34, 400, 316, 300, 168, 168, 117, 475, 62, 396, 423, 479, 69, 208, 88, 447, 371, 196, 389, 241, 486, 459, 423, 413, 373, 203, 77, 320, 299, 273, 450, 371, 432, 325, 237, 161, 137, 151, 111, 57, 171, 339, 285, 319, 404, 373, 173, 384, 270, 285, 359, 395, 121, 373, 189, 489, 132, 454, 396, 96, 429, 452, 432, 248, 211, 189, 477, 128, 296, 379, 219, 155, 379, 163, 401, 91, 211, 388, 364, 183, 68, 59, 416, 253, 404, 169, 16, 412, 352, 96, 495, 499, 34, 465, 97, 373, 195, 331, 28, 257, 169, 477, 326, 376, 32, 198, 67, 395, 169, 15, 360, 356, 42, 254, 157, 326, 462, 42, 154, 477, 126, 401, 77, 345, 295, 179, 109, 408, 154, 99, 125, 214, 70, 93, 16, 172, 148, 158, 149, 338, 344, 276, 213, 484, 89, 170, 110, 178, 413, 484, 335, 156, 420, 434, 97, 425, 101, 60, 60, 366, 289, 477, 261, 413, 293, 169, 313, 359, 202, 414, 445, 455, 363, 230, 328, 1, 229, 129, 21, 498, 248, 251, 105, 72, 66, 380, 82, 433, 224, 4, 437, 436, 327, 255, 403, 172, 117, 305, 203, 319, 474, 93, 331, 69, 463, 419, 26, 229, 457, 412, 58, 193, 67, 358, 292, 107, 5, 291, 416, 293, 6, 73, 242, 182, 101, 141, 194, 265, 91, 56, 250]

print("Insertion sort: ", insertion_sort(arr1))
print("Bubble sort: ", bubble_sort(arr2))