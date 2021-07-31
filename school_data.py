# school_data.py
# AUTHOR NAME: Melissa Liao
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np

school_dict = {
'Centennial High School' : 1224,
'Robert Thirsk School' : 1679,
'Louise Dean School' : 9626,
'Queen Elizabeth High School' : 9806,
'Forest Lawn High School' : 9813,
'Crescent Heights High School' : 9815,
'Western Canada High School' : 9816,
'Central Memorial High School' : 9823,
'James Fowler High School' : 9825,
'Ernest Manning High School' : 9826,
'William Aberhart High School' : 9829,
'National Sport School' : 9830,
'Henry Wise Wood High School' : 9836,
'Bowness High School' : 9847,
'Lord Beaverbrook High School' : 9850,
'Jack James High School' : 9856,
'Sir Winston Churchill High School' : 9857,
'Dr. E. P. Scarlett High School' : 9858,
'John G Diefenbaker High School' : 9860,
'Lester B. Pearson High School' : 9865,
}

school_2013 = [
591, 572, 558, 
472, 346, 0, 
45, 57, 52, 
160, 176, 189, 
426, 483, 567, 
620, 584, 585, 
658, 631, 632, 
289, 280, 311, 
496, 465, 528, 
523, 467, 517, 
487, 413, 457, 
29, 29, 45, 
399, 361, 380, 
210, 225, 359, 
657, 566, 501, 
163, 146, 228, 
587, 611, 648, 
514, 577, 522, 
435, 364, 509, 
504, 530, 512
]

school_2014 = [
599, 592, 598, 
444, 452, 341, 
40, 49, 55, 
151, 137, 173, 
430, 404, 572, 
662, 611, 602, 
618, 639, 605, 
323, 370, 395, 
422, 437, 524, 
522, 549, 529, 
537, 502, 416, 
36, 44, 44, 
362, 371, 354, 
219, 200, 222, 
569, 619, 562, 
131, 164, 208, 
604, 641, 720, 
549, 541, 581, 
438, 431, 459, 
518, 501, 565
]

school_2015 = [
558, 585, 598, 
419, 411, 463, 
29, 36, 68, 
137, 115, 106, 
373, 403, 532, 
659, 643, 583, 
624, 610, 594, 
271, 227, 316, 
564, 383, 455, 
565, 530, 543, 
469, 491, 499, 
48, 37, 43, 
361, 337, 373, 
215, 209, 212, 
578, 489, 590, 
116, 126, 201, 
726, 626, 651, 
515, 523, 529, 
461, 406, 494, 
552, 495, 515
]

school_2016 = [
625, 555, 600, 
345, 396, 436, 
16, 47, 56, 
155, 93, 137, 
431, 384, 567, 
440, 514, 659, 
682, 571, 630, 
183, 210, 230, 
197, 237, 459, 
581, 583, 546, 
460, 438, 499, 
41, 46, 48, 
341, 367, 377, 
233, 207, 221, 
535, 546, 543, 
74, 95, 179, 
691, 740, 680, 
556, 528, 568, 
420, 456, 511, 
459, 512, 564
]

school_2017 = [
611, 617, 582, 
433, 374, 450, 
15, 48, 58, 
115, 123, 106, 
395, 378, 531, 
408, 388, 529, 
798, 665, 636, 
355, 368, 491, 
215, 193, 330, 
607, 557, 555, 
491, 439, 423, 
45, 50, 56, 
422, 338, 390, 
249, 241, 232, 
583, 506, 534, 
127, 127, 191, 
706, 680, 763, 
546, 580, 549, 
459, 418, 517, 
497, 423, 582
]

school_2018 = [
485, 540, 582, 
398, 423, 391, 
23, 25, 58, 
150, 83, 120, 
395, 402, 527, 
568, 426, 510, 
716, 688, 651, 
387, 388, 419, 
242, 204, 254, 
685, 576, 535, 
437, 473, 428, 
38, 45, 57, 
417, 391, 398, 
386, 238, 249, 
229, 250, 495, 
81, 112, 135, 
703, 705, 744, 
533, 496, 580, 
443, 438, 460, 
551, 456, 473
]

school_2019 = [
463, 481, 556, 
355, 430, 455, 
13, 23, 52, 
146, 146, 127, 
383, 397, 441, 
556, 615, 530, 
723, 724, 798, 
391, 391, 409, 
251, 234, 322, 
674, 692, 629, 
476, 447, 507, 
61, 56, 69, 
458, 434, 424, 
391, 381, 254, 
241, 245, 299, 
102, 77, 146, 
749, 677, 744, 
488, 514, 503, 
474, 449, 531, 
535, 528, 553
]

school_2020 = [
455, 436, 437, 
360, 352, 437, 
12, 21, 34, 
137, 143, 142, 
378, 361, 438, 
565, 555, 629, 
690, 727, 734, 
543, 401, 459, 
290, 234, 315, 
491, 662, 680, 
420, 465, 434, 
34, 59, 64, 
532, 449, 431, 
402, 382, 364, 
482, 251, 293, 
128, 102, 144, 
739, 746, 709, 
540, 463, 503, 
452, 482, 475, 
537, 533, 559
]

# Convert dictionary list into an array list
array_dict = np.array(list(school_dict.items()))
array_2013 = np.array(school_2013).reshape((20,3))
array_2014 = np.array(school_2014).reshape((20,3))
array_2015 = np.array(school_2015).reshape((20,3))
array_2016 = np.array(school_2016).reshape((20,3))
array_2017 = np.array(school_2017).reshape((20,3))
array_2018 = np.array(school_2018).reshape((20,3))
array_2019 = np.array(school_2019).reshape((20,3))
array_2020 = np.array(school_2020).reshape((20,3))

# Concatenating all year arrays into one data
school_data = np.array([array_2013, array_2014, array_2015, array_2016, array_2017, array_2018, array_2019, array_2020])

def main():
    print("ENSF 592 School Enrollment Statistics")
    
    # Print Stage 1 requirements here
    print("Shape of full data array: ", school_data.shape)
    print("Dimensions of full data array: ", school_data.ndim)

    # Prompt for user input
    while True:
        input_school = input("Please enter the high school name or school code: ")
        if input_school not in array_dict:
            # Will prompt a ValueError message if user doesn't input exact school name or code
            ValueError(print("You must enter a valid school name or code."))
        else:
            break
    
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # To find the index of the school chosen by the user
    chosen_school = np.where(array_dict == input_school)
    # To look for the chosen school's name/code and its data
    school_info = array_dict[chosen_school[0]]
    chosen_school_data = school_data[:, chosen_school[0] , :]

    print("School Name: {0}, School Code: {1}".format(school_info[0,0], school_info[0,1]))
    print("Mean enrollment for Grade 10: ", np.mean(chosen_school_data[:, 0, 0]))
    print("Mean enrollment for Grade 11: ", np.mean(chosen_school_data[:, 0, 1])) 
    print("Mean enrollment for Grade 12: ", np.mean(chosen_school_data[:, 0, 2]))
    print("Highest enrollment for a single grade: ", np.max(chosen_school_data))
    print("Lowest enrollment for a single grade: ", np.min(chosen_school_data))

    # To find enrollment for each year
    for i in range(8):
        print("Total enrollment for {0}: {1}".format(2013 + i, np.sum(chosen_school_data[i, :, :])))
    
    if np.any(chosen_school_data > 500):
        print("For all enrollments over 500, the median value was: ", np.median(chosen_school_data[chosen_school_data > 500]))
    else:
        print("No enrollments over 500.")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    print("Mean enrollment in 2013: ", np.mean(school_data[0, :, :]))
    print("Mean enrollment in 2020: ", np.mean(school_data[7, :, :]))
    print("Total graduating class of 2020: ", np.sum(school_data[7, :, 2]))
    print("Highest enrollment for a single grade: ", np.max(school_data))
    print("Lowest enrollment for a single grade: ", np.min(school_data))


if __name__ == '__main__':
    main()
