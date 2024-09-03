unit Main;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons,
  ExtCtrls;

type

  { TFCalculator }

  TFCalculator = class(TForm)
    EConclusion: TEdit;
    ImageList1: TImageList;
    BOne: TSpeedButton;
    BTwo: TSpeedButton;
    BThree: TSpeedButton;
    BFour: TSpeedButton;
    BFive: TSpeedButton;
    BSix: TSpeedButton;
    BSeven: TSpeedButton;
    BEight: TSpeedButton;
    BNine: TSpeedButton;
    BZero: TSpeedButton;
    BComma: TSpeedButton;
    BPlus: TSpeedButton;
    BMinus: TSpeedButton;
    BMultiplication: TSpeedButton;
    BDivision: TSpeedButton;
    BBackspace: TSpeedButton;
    BCE: TSpeedButton;
    BC: TSpeedButton;
    BSqrt: TSpeedButton;
    BRoot: TSpeedButton;
    BFormula: TSpeedButton;
    BEqually: TSpeedButton;
    procedure BBackspaceClick(Sender: TObject);
    procedure BCClick(Sender: TObject);
    procedure BCEClick(Sender: TObject);
    procedure BCommaClick(Sender: TObject);
    procedure BEquallyClick(Sender: TObject);
    procedure BFormulaClick(Sender: TObject);
    procedure BRootClick(Sender: TObject);
    procedure BSqrtClick(Sender: TObject);
    procedure ClickButton(Sender:TObject);
    procedure ClickAction(Sender:TObject);
    procedure ErrorMessage();

  private

  public
  end;

  var
    FCalculator: TFCalculator;
    NumbA, NumbB, Result: Real;
    ActionBut: String;
    Devis: Boolean;


implementation

{$R *.lfm}

{ TFCalculator }
procedure TFCalculator.ClickAction(Sender:TObject);
begin
  if EConclusion.Text <> '' then
  begin
     ActionBut := (Sender as TSpeedButton).Caption;
     NumbA := StrToFloat(EConclusion.Text);
     EConclusion.Clear;
     case ActionBut of
     '+' : Result += NumbA;
     '-' : begin if Result = 0 then Result:= NumbA else Result -= NumbA; end;
     '*' : begin if Result = 0 then Result:= NumbA else Result *= NumbA; end;
     '/' : begin if (Result = 0) and (Devis = False) then begin Result := NumbA; Devis := True; end else if NumbA <> 0 then Result /= NumbA else ErrorMessage(); end;
     end;
  end
  else if (Pos('-', EConclusion.Text) = 0) and ((Sender as TSpeedButton).Caption = '-') then
  EConclusion.Text := EConclusion.Text + (Sender as TSpeedButton).Caption;
end;

procedure TFCalculator.ClickButton(Sender:TObject);
begin
  if EConclusion.Text <> '0' then
  EConclusion.Text := EConclusion.Text + (Sender as TSpeedButton).Caption
  else
  EConclusion.Text := (Sender as TSpeedButton).Caption;
end;

procedure TFCalculator.BBackspaceClick(Sender: TObject);
var str: String;
begin
  str := EConclusion.Text;
  if str <> '' then
  Delete(str, Length(str),1);
  EConclusion.Text := str;
end;

procedure TFCalculator.BCClick(Sender: TObject);
begin
  EConclusion.Clear;
  NumbA := 0;
  NumbB := 0;
  Result := 0;
end;

procedure TFCalculator.BCEClick(Sender: TObject);
begin
  EConclusion.Clear;
end;

procedure TFCalculator.BCommaClick(Sender: TObject);
begin
  if (Pos(',', EConclusion.Text) = 0) and (EConclusion.Text <> '') then
  begin
     if (Pos('-', EConclusion.Text) = 1) and (Length(EConclusion.Text) = 1) then
     EConclusion.Text := EConclusion.Text + '0';
    EConclusion.Text := EConclusion.Text + (Sender as TSpeedButton).Caption;
  end;
end;

procedure TFCalculator.BEquallyClick(Sender: TObject);
begin
  if EConclusion.Text <> '' then
  begin
     NumbB := StrToFloat(EConclusion.Text);
     EConclusion.Clear;
     case ActionBut of
     '+' : Result:= Result + NumbB;
     '-' : Result:= Result - NumbB;
     '*' : Result:= Result * NumbB;
     '/' : begin if NumbB = 0 then begin ErrorMessage(); Exit; end else Result:= Result / NumbB; Devis := False; end;
     '': Result:= NumbB;
     end;
     EConclusion.Text := FloatToStr(Result);
     Result:= 0;
  end;
end;

procedure TFCalculator.BFormulaClick(Sender: TObject);
begin
  if EConclusion.Text <> '' then
  begin
      NumbA := StrToFloat(EConclusion.Text);
      if NumbA = 0 then
      begin
        ErrorMessage();
      end
      else
      begin
        NumbA := 1/NumbA;
        EConclusion.Text := FloatToStr(NumbA);
      end;
  end;
end;

procedure TFCalculator.BRootClick(Sender: TObject);
begin
  if EConclusion.Text <> '' then
  begin
     NumbA := StrToFloat(EConclusion.Text);
     NumbA := Sqr(NumbA);
     EConclusion.Text := FloatToStr(NumbA);
  end;
end;

procedure TFCalculator.BSqrtClick(Sender: TObject);
begin
  if EConclusion.Text <> '' then
  begin
      if Pos('-', EConclusion.Text) = 1 then
      ErrorMessage()
      else
      begin
         NumbA := StrToFloat(EConclusion.Text);
         NumbA := Sqrt(NumbA);
         EConclusion.Text := FloatToStr(NumbA);
      end;
  end;
end;

procedure TFCalculator.ErrorMessage();
begin
    EConclusion.Text := 'Незя, ай-яй-яй.';
    Application.ProcessMessages();
    Sleep(1500);
    EConclusion.Text := '';
    Result:= 0;
    Devis := False;
end;

begin

end.

