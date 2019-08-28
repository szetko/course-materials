void TileMap::LoadMapFromFile(String^ mapFileName)
{
    // Creating a new stream reader and opening the map file
	StreamReader^ sr = File::OpenText(mapFileName);

    // Will hold each line read from the input file
	String^ currentLine = "";

    // Will hold the individual strings returned by splitting currentLine on comma
	array<String^>^ indexHolder = gcnew array<String^>(nCols);

    // Keeps track of which row of the map you are filling
	int rowCounter = 0;

    // While loop runs until all lines have been read from the file
	while (currentLine = sr->ReadLine())
	{
        // Split currentLine on comma
		indexHolder = currentLine->Split(',');
        
        // Loop through the number of columns
		for (int columnCounter = 0; columnCounter < nCols; columnCounter++)
		{
            // Get the index value and convert to int
			int indexValue = Convert::ToInt16(indexHolder[columnCounter]);
            
            // Set the map's column and row value to the index value
			map[columnCounter, rowCounter] = indexValue;
		}
        // Increment the loop counter
		rowCounter++;
	}
}

