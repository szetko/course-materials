void TileMap::LoadMapFromFile(String^ mapFileName)
{
	StreamReader^ sr = File::OpenText(mapFileName);

	String^ currentLine = "";

	array<String^>^ indexHolder = gcnew array<String^>(nCols);

	int rowCounter = 0;

	while (currentLine = sr->ReadLine())
	{
		indexHolder = currentLine->Split(',');
		for (int columnCounter = 0; columnCounter < nCols; columnCounter++)
		{
			int indexValue = Convert::ToInt16(indexHolder[columnCounter]);
			map[columnCounter, rowCounter] = indexValue;
		}
		rowCounter++;
	}
}
