unit Main;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, Buttons,
  Grids, edit;

type

  { TfMain }

  TfMain = class(TForm)
    Panel1: TPanel;
    bAdd: TSpeedButton;
    bEdit: TSpeedButton;
    bDel: TSpeedButton;
    bSort: TSpeedButton;
    SG: TStringGrid;
    procedure bAddClick(Sender: TObject);
    procedure bDelClick(Sender: TObject);
    procedure bEditClick(Sender: TObject);
    procedure bSortClick(Sender: TObject);
    procedure FormClose(Sender: TObject; var CloseAction: TCloseAction);
    procedure FormCreate(Sender: TObject);
  private

  public

  end;

type
  Game = record
    Title: string[100];
    Genre: string[100];
    Developer: string[100];
    Platform: string[20];
    RussianLangueg: boolean;
    Date: TDateTime;
    Rate: real;
  end; //record


var
  fMain: TfMain;
  adres:string;

implementation

{$R *.lfm}

{ TfMain }


procedure TfMain.bAddClick(Sender: TObject);
begin
  fEdit.eTitle.Text:= '';
  fEdit.cbGenre.ItemIndex:= 0;
  fEdit.eDeveloper.Text:= '';
  fEdit.cbPlatform.ItemIndex:= 0;
  fEdit.CheckLangueg.Checked:= False;
  fEdit.deDate.Text:= '';
  fEdit.fseRate.Value := 0;
  fEdit.ModalResult:= mrNone;
  fEdit.ShowModal;
  if (fEdit.eTitle.Text= '') or (fEdit.eDeveloper.Text= '') or (fEdit.cbPlatform.Text= '') or (fEdit.deDate.Text= '') or (fEdit.fseRate.Text= '') then exit;
  if fEdit.ModalResult <> mrOk then exit;
  SG.RowCount:= SG.RowCount + 1;
  SG.Cells[0, SG.RowCount-1]:= fEdit.eTitle.Text;
  SG.Cells[1, SG.RowCount-1]:= fEdit.cbGenre.Text;
  SG.Cells[2, SG.RowCount-1]:= fEdit.eDeveloper.Text;
  SG.Cells[3, SG.RowCount-1]:= fEdit.cbPlatform.Text;
  if fEdit.CheckLangueg.Checked then SG.Cells[4, SG.RowCount-1]:= 'Есть'
  else SG.Cells[4, SG.RowCount-1]:= 'Отсутствует';
  SG.Cells[5, SG.RowCount-1]:= fEdit.deDate.Text;
  SG.Cells[6, SG.RowCount-1]:= fEdit.fseRate.Text;
end;

procedure TfMain.bDelClick(Sender: TObject);
begin
  if SG.RowCount = 1 then exit;
  if MessageDlg('Требуется подтверждение',
                'Вы действительно хотите удалить контакт "' +
                SG.Cells[0, SG.Row] + '"?',
      mtConfirmation, [mbYes, mbNo, mbIgnore], 0) = mrYes then
         SG.DeleteRow(SG.Row);
end;


procedure TfMain.bEditClick(Sender: TObject);
begin
  if SG.RowCount = 1 then exit;
  fEdit.eTitle.Text:= SG.Cells[0, SG.Row];
  fEdit.cbGenre.Text:= SG.Cells[1, SG.Row];
  fEdit.eDeveloper.Text:= SG.Cells[2, SG.Row];
  fEdit.cbPlatform.Text:= SG.Cells[3, SG.Row];
  if SG.Cells[4, SG.Row] = 'Есть' then fEdit.CheckLangueg.Checked:= True
  else fEdit.CheckLangueg.Checked:= False;
  fEdit.deDate.Text:= SG.Cells[5, SG.Row];
  fEdit.fseRate.Text:= SG.Cells[6, SG.Row];
  fEdit.ModalResult:= mrNone;
  fEdit.ShowModal;
  if fEdit.ModalResult = mrOk then begin
    SG.Cells[0, SG.Row]:= fEdit.eTitle.Text;
    SG.Cells[1, SG.Row]:= fEdit.cbGenre.Text;
    SG.Cells[2, SG.Row]:= fEdit.eDeveloper.Text;
    SG.Cells[3, SG.Row]:= fEdit.cbPlatform.Text;
    if fEdit.CheckLangueg.Checked then SG.Cells[4, SG.RowCount-1]:= 'Есть'
    else SG.Cells[4, SG.Row]:= 'Отсутствует';
    SG.Cells[5, SG.Row]:= fEdit.deDate.Text;
    SG.Cells[6, SG.Row]:= fEdit.fseRate.Text;
  end;
end;

procedure TfMain.bSortClick(Sender: TObject);
begin
  if SG.RowCount = 1 then exit;
  SG.SortColRow(true, 0);
end;

procedure TfMain.FormClose(Sender: TObject; var CloseAction: TCloseAction);
var
  InfoGame: Game;
  f: file of Game;
  i: integer;
begin
  if SG.RowCount = 1 then exit;
  try
    AssignFile(f, adres + 'games.dat');
    Rewrite(f);
    for i:= 1 to SG.RowCount-1 do begin
      InfoGame.Title:= SG.Cells[0, i];
      InfoGame.Genre:= SG.Cells[1, i];
      InfoGame.Developer:= SG.Cells[2, i];
      InfoGame.Platform:= SG.Cells[3, i];
      if SG.Cells[4, i] = 'Есть.' then InfoGame.RussianLangueg:= True
      else InfoGame.RussianLangueg:= False;
      InfoGame.Date:= StrToDateTime(SG.Cells[5, i]);
      InfoGame.Rate:= StrToFloat(SG.Cells[6, i]);
      Write(f, InfoGame);
    end;
  finally
    CloseFile(f);
  end;
end;

procedure TfMain.FormCreate(Sender: TObject);
var
  InfoGame: Game;
  f: file of Game;
  i: integer;
begin
  adres:= ExtractFilePath(ParamStr(0));
  SG.Cells[0, 0]:= 'Название игры';
  SG.Cells[1, 0]:= 'Жанр';
  SG.Cells[2, 0]:= 'Разработчик';
  SG.Cells[3, 0]:= 'Платформа';
  SG.Cells[4, 0]:= 'Руский язык';
  SG.Cells[5, 0]:= 'Дата выхода';
  SG.Cells[6, 0]:= 'Оценка';
  SG.ColWidths[0]:= 240;
  SG.ColWidths[1]:= 240;
  SG.ColWidths[2]:= 240;
  SG.ColWidths[3]:= 130;
  SG.ColWidths[4]:= 150;
  SG.ColWidths[5]:= 150;
  SG.ColWidths[6]:= 100;
  if not FileExists(adres + 'games.dat') then exit;
  try
    AssignFile(f, adres + 'games.dat');
    Reset(f);
    while not Eof(f) do begin
      Read(f, InfoGame);
        SG.RowCount:= SG.RowCount + 1;
        SG.Cells[0, SG.RowCount-1]:= InfoGame.Title;
        SG.Cells[1, SG.RowCount-1]:= InfoGame.Genre;
        SG.Cells[2, SG.RowCount-1]:= InfoGame.Developer;
        SG.Cells[3, SG.RowCount-1]:= InfoGame.Platform;
         if InfoGame.RussianLangueg = True then SG.Cells[4, SG.RowCount-1]:= 'Есть'
        else SG.Cells[4, SG.RowCount-1]:= 'Отсутствует';
        SG.Cells[5, SG.RowCount-1]:= DateTimeToStr(InfoGame.Date);
        SG.Cells[6, SG.RowCount-1]:= FloatToStr(InfoGame.Rate);
    end;
  finally
    CloseFile(f);
  end;
end;


end.


