#include "Form1.h"

using namespace System;
using namespace System::Windows::Forms;


[STAThread]
void Main(array<String^>^ args)
{
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);

	InheritanceApproachAvoid::Form1 form;
	Application::Run(%form);
}