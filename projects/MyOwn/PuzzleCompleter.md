# Puzzle Completer

This project is intended to take the original image of a puzzle and your already solved puzzle with missing pieces. 

The program will find the pieces that you're missing and it will compute the shape and size (if height and width provided) of the missing pieces, you'll eventually be able to export it into a PDF and print it so you can completely solve your puzzle :)

The needed steps to compute this are:

- Find the shape of both images and scale them to the same size.

- Overlap images to find the missing pieces.

- Find shape of missing pieces.

- Scale back shapes to centimeters.

- Export to pdf.