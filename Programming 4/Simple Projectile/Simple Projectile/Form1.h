#pragma once

namespace SimpleProjectile {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for Form1
	/// </summary>
	public ref class Form1 : public System::Windows::Forms::Form
	{
	public:
		Form1(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~Form1()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::Button^  btnLaunch;
	protected:
	private: System::Windows::Forms::Label^  label1;
	private: System::Windows::Forms::NumericUpDown^  spinAngle;
	private: System::Windows::Forms::NumericUpDown^  spinPower;
	private: System::Windows::Forms::Label^  label2;
	private: System::Windows::Forms::PictureBox^  pbxCircle;
	private: System::Windows::Forms::Timer^  timer1;
	private: System::Windows::Forms::PictureBox^  pictureBox1;
	private: System::Windows::Forms::PictureBox^  pictureBox2;



	private: System::ComponentModel::IContainer^  components;


	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>


#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			this->components = (gcnew System::ComponentModel::Container());
			System::ComponentModel::ComponentResourceManager^  resources = (gcnew System::ComponentModel::ComponentResourceManager(Form1::typeid));
			this->btnLaunch = (gcnew System::Windows::Forms::Button());
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->spinAngle = (gcnew System::Windows::Forms::NumericUpDown());
			this->spinPower = (gcnew System::Windows::Forms::NumericUpDown());
			this->label2 = (gcnew System::Windows::Forms::Label());
			this->pbxCircle = (gcnew System::Windows::Forms::PictureBox());
			this->timer1 = (gcnew System::Windows::Forms::Timer(this->components));
			this->pictureBox1 = (gcnew System::Windows::Forms::PictureBox());
			this->pictureBox2 = (gcnew System::Windows::Forms::PictureBox());
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->spinAngle))->BeginInit();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->spinPower))->BeginInit();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pbxCircle))->BeginInit();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pictureBox1))->BeginInit();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pictureBox2))->BeginInit();
			this->SuspendLayout();
			// 
			// btnLaunch
			// 
			this->btnLaunch->Location = System::Drawing::Point(39, 43);
			this->btnLaunch->Name = L"btnLaunch";
			this->btnLaunch->Size = System::Drawing::Size(108, 41);
			this->btnLaunch->TabIndex = 0;
			this->btnLaunch->Text = L"Launch";
			this->btnLaunch->UseVisualStyleBackColor = true;
			this->btnLaunch->Click += gcnew System::EventHandler(this, &Form1::btnLaunch_Click);
			// 
			// label1
			// 
			this->label1->AutoSize = true;
			this->label1->ForeColor = System::Drawing::SystemColors::ButtonHighlight;
			this->label1->Location = System::Drawing::Point(188, 54);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(57, 24);
			this->label1->TabIndex = 1;
			this->label1->Text = L"Angle";
			// 
			// spinAngle
			// 
			this->spinAngle->Location = System::Drawing::Point(250, 52);
			this->spinAngle->Name = L"spinAngle";
			this->spinAngle->Size = System::Drawing::Size(120, 32);
			this->spinAngle->TabIndex = 2;
			this->spinAngle->Value = System::Decimal(gcnew cli::array< System::Int32 >(4) { 45, 0, 0, 0 });
			// 
			// spinPower
			// 
			this->spinPower->Location = System::Drawing::Point(490, 52);
			this->spinPower->Name = L"spinPower";
			this->spinPower->Size = System::Drawing::Size(120, 32);
			this->spinPower->TabIndex = 4;
			this->spinPower->Value = System::Decimal(gcnew cli::array< System::Int32 >(4) { 10, 0, 0, 0 });
			// 
			// label2
			// 
			this->label2->AutoSize = true;
			this->label2->ForeColor = System::Drawing::SystemColors::ButtonHighlight;
			this->label2->Location = System::Drawing::Point(428, 54);
			this->label2->Name = L"label2";
			this->label2->Size = System::Drawing::Size(62, 24);
			this->label2->TabIndex = 3;
			this->label2->Text = L"Power";
			// 
			// pbxCircle
			// 
			this->pbxCircle->Image = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"pbxCircle.Image")));
			this->pbxCircle->Location = System::Drawing::Point(19, 445);
			this->pbxCircle->Name = L"pbxCircle";
			this->pbxCircle->Size = System::Drawing::Size(128, 127);
			this->pbxCircle->SizeMode = System::Windows::Forms::PictureBoxSizeMode::AutoSize;
			this->pbxCircle->TabIndex = 6;
			this->pbxCircle->TabStop = false;
			// 
			// timer1
			// 
			this->timer1->Tick += gcnew System::EventHandler(this, &Form1::timer1_Tick);
			// 
			// pictureBox1
			// 
			this->pictureBox1->Image = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"pictureBox1.Image")));
			this->pictureBox1->Location = System::Drawing::Point(833, 177);
			this->pictureBox1->Name = L"pictureBox1";
			this->pictureBox1->Size = System::Drawing::Size(32, 255);
			this->pictureBox1->SizeMode = System::Windows::Forms::PictureBoxSizeMode::AutoSize;
			this->pictureBox1->TabIndex = 5;
			this->pictureBox1->TabStop = false;
			// 
			// pictureBox2
			// 
			this->pictureBox2->BackColor = System::Drawing::Color::Transparent;
			this->pictureBox2->Image = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"pictureBox2.Image")));
			this->pictureBox2->Location = System::Drawing::Point(863, 177);
			this->pictureBox2->Name = L"pictureBox2";
			this->pictureBox2->Size = System::Drawing::Size(31, 256);
			this->pictureBox2->SizeMode = System::Windows::Forms::PictureBoxSizeMode::AutoSize;
			this->pictureBox2->TabIndex = 7;
			this->pictureBox2->TabStop = false;
			// 
			// Form1
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(10, 24);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->BackColor = System::Drawing::SystemColors::ActiveCaptionText;
			this->ClientSize = System::Drawing::Size(906, 584);
			this->Controls->Add(this->pictureBox2);
			this->Controls->Add(this->pbxCircle);
			this->Controls->Add(this->spinPower);
			this->Controls->Add(this->label2);
			this->Controls->Add(this->spinAngle);
			this->Controls->Add(this->label1);
			this->Controls->Add(this->btnLaunch);
			this->Controls->Add(this->pictureBox1);
			this->Font = (gcnew System::Drawing::Font(L"Calibri", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->Margin = System::Windows::Forms::Padding(4);
			this->Name = L"Form1";
			this->Text = L"Simple Projectile - Send the circle through the hoop...";
			this->WindowState = System::Windows::Forms::FormWindowState::Maximized;
			this->Load += gcnew System::EventHandler(this, &Form1::Form1_Load);
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->spinAngle))->EndInit();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->spinPower))->EndInit();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pbxCircle))->EndInit();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pictureBox1))->EndInit();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pictureBox2))->EndInit();
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
		// Class Data Members ('global variables')
		Point circleStartPosition;
		int xVelocity;
		int yVelocity;
		int gravity;

	//===========================================================================================
	// Form_Load
	//===========================================================================================
	private: System::Void Form1_Load(System::Object^  sender, System::EventArgs^  e) 
	{
		// Init. Save starting location of pbxCircle for reset, below.
		circleStartPosition = Point(pbxCircle->Left, pbxCircle->Top);
		gravity = 3;
	} // end Form Load


	//===========================================================================================
	// Launch button click handler
	//===========================================================================================
	private: System::Void btnLaunch_Click(System::Object^  sender, System::EventArgs^  e) 
	{
		// Read the input values
		// spinbox::Value is of type decimal; we don't need that much precision, so cast to int
		int angle = (int)spinAngle->Value;
		int power = (int)spinPower->Value;

		// Initialise the global xVelocity and yVelocity variables
		// based on angle and power.
		double radianAngle = -(angle * 0.01745);
	
		xVelocity = Math::Cos(radianAngle) * power;
		yVelocity = Math::Sin(radianAngle) * power;

		// Start the timer
		timer1->Enabled = true;

	} // end launch button click handler

	//===========================================================================================
	// Timer tick handler
	//===========================================================================================
	private: System::Void timer1_Tick(System::Object^  sender, System::EventArgs^  e)
	{
		// Move the circle. Update all state as required
		pbxCircle->Top += yVelocity;
		pbxCircle->Left += xVelocity;
		yVelocity += gravity;

		// The circle is gone. Reset.
		if (pbxCircle->Top > Height)
		{
			// Stop the timer
			timer1->Enabled = false;

			// Reposition the circle
			pbxCircle->Left = circleStartPosition.X;
			pbxCircle->Top = circleStartPosition.Y;
		}

	} // end timer handler

}; // end Form class
} // end namespace
