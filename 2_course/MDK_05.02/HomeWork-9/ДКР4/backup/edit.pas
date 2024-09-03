unit Edit;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons,
  EditBtn, Spin, ExtCtrls, mmSystem, enot;

type

  { TfEdit }

  TfEdit = class(TForm)
    bCancel: TBitBtn;
    bSave: TBitBtn;
    CheckLangueg: TCheckBox;
    cbPlatform: TComboBox;
    cbGenre: TComboBox;
    deDate: TDateEdit;
    eDeveloper: TEdit;
    eTitle: TEdit;
    fseRate: TFloatSpinEdit;
    Image1: TImage;
    Image2: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    procedure FormShow(Sender: TObject);
    procedure Image1Click(Sender: TObject);
    procedure Image2Click(Sender: TObject);
  private

  public

  end;

var
  fEdit: TfEdit;

implementation

{$R *.lfm}

{ TfEdit }

procedure TfEdit.FormShow(Sender: TObject);
begin
   eTitle.SetFocus;
end;

procedure TfEdit.Image1Click(Sender: TObject);
begin
  sndPlaySound('cricket-sound.wav', SND_SYNC or SND_NODEFAULT);
end;

procedure TfEdit.Image2Click(Sender: TObject);
begin
  fEnot.ShowModal;
end;

end.

