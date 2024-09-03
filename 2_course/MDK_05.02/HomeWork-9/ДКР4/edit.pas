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
    iForest: TImage;
    iCookie: TImage;
    lTitle: TLabel;
    lGener: TLabel;
    lDeveloper: TLabel;
    lPlatform: TLabel;
    lLangueg: TLabel;
    lRate: TLabel;
    lDate: TLabel;
    procedure FormShow(Sender: TObject);
    procedure iForestClick(Sender: TObject);
    procedure iCookieClick(Sender: TObject);
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

procedure TfEdit.iForestClick(Sender: TObject);
begin
  sndPlaySound('cricket-sound.wav', SND_SYNC or SND_NODEFAULT);
end;

procedure TfEdit.iCookieClick(Sender: TObject);
begin
  fEnot.ShowModal;
end;

end.

