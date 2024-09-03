unit Main;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ComCtrls,
  Spin, Buttons, Math;

type

  { TfCalculator }

  TfCalculator = class(TForm)
    bbCalculate: TBitBtn;
    bbClear: TBitBtn;
    CBTime: TComboBox;
    CBTypeProcent: TComboBox;
    eMoney: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    mAnswer: TMemo;
    mTitle: TMemo;
    seProcent: TSpinEdit;
    seDate: TSpinEdit;
    procedure bbCalculateClick(Sender: TObject);
    procedure bbClearClick(Sender: TObject);
    procedure eMoneyKeyPress(Sender: TObject; var Key: char);
    procedure Clear();
  private

  public

  end;

var
  fCalculator: TfCalculator;


implementation

{$R *.lfm}

{ TfCalculator }

procedure TfCalculator.eMoneyKeyPress(Sender: TObject; var Key: char);
begin
  case Key of
  '0'..'9': key:=key;
  ',','.': if Pos('.', eMoney.Text) = 0 then key:='.' else key:=#0;
  #8: key:=key;
  else key:=#0;
  end;
end;

procedure TfCalculator.bbClearClick(Sender: TObject);
begin
  Clear();
  mTitle.Clear;
  mAnswer.Clear;
end;

procedure TfCalculator.Clear();
begin
  eMoney.Clear;
  seDate.Value := 0;
  seProcent.Value := 0;
  CBTypeProcent.ItemIndex := 0;
  CBTime.ItemIndex := 0;
end;

procedure TfCalculator.bbCalculateClick(Sender: TObject);
var Money, Procent, Date: real;
begin
  if eMoney.Text <> '' then
  begin
    Money := StrToFloat(eMoney.Text);
    Procent := StrToFloat(seProcent.Text)/100;
    Date := StrToFloat(seDate.Text);
    mTitle.Text := CBTypeProcent.Text;
    mAnswer.Text := 'Исходная сумма ' + eMoney.Text + ' руб.' +  #13;
    mAnswer.Text := mAnswer.Text + 'Проценты: ' + seProcent.Text + '%' + #13;
    // простые проценты
    if CBTypeProcent.ItemIndex = 0 then
    begin
      if CBTime.ItemIndex = 0 then
      begin
        mAnswer.Text := mAnswer.Text + 'Период в месяцах: ' + seDate.Text + '.' + #13;
        mAnswer.Text := mAnswer.Text + 'Итого: ' + FloatToStr(RoundTo(Money * (1 + Procent * Date/12), -2)) + '.';
      end
      else if CBTime.ItemIndex = 1 then
      begin
        mAnswer.Text := mAnswer.Text + 'Период в годах: ' + seDate.Text + '.' + #13;
        mAnswer.Text := mAnswer.Text + 'Итого: ' + FloatToStr(RoundTo(Money * (1 + Procent * Date), -2)) + '.';
      end
    end
    // сложные проценты
    else
    begin
       if CBTime.ItemIndex = 0 then
      begin
        mAnswer.Text := mAnswer.Text + 'Период в месяцах: ' + seDate.Text + '.' + #13;
        mAnswer.Text := mAnswer.Text + 'Итого: ' + FloatToStr(RoundTo(Money *(Power(1 + Procent, Date/12)), -2)) + '.';
      end
      else if CBTime.ItemIndex = 1 then
      begin
        mAnswer.Text := mAnswer.Text + 'Период в годах: ' + seDate.Text + '.' + #13;
        mAnswer.Text := mAnswer.Text + 'Итого: ' + FloatToStr(RoundTo(Money *(Power(1 + Procent, Date)), -2)) + '.';
      end
    end;

    Clear();
  end;
end;


end.

