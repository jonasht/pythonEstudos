
import re

def validate_credit_card_number(card_number):
    card_number = re.sub(r'[\D]', '', card_number)
    visa_pattern = re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$')
    mastercard_pattern = re.compile(r'^5[1-5][0-9]{14}$')
    hipercard_pattern = re.compile(r'^(606282\d{10}(\d{3})?)|(3841\d{15})$')
    amex_pattern = re.compile(r'^3[47][0-9]{13}$')
    diners_pattern = re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$')
    elo_pattern = re.compile(r'^((636368)|(438935)|(504175)|(451416)|(509048)|(509067)|(509049)|(509069)|(509050)|(509074)|(509068)|(509040)|(509045)|(509051)|(509046)|(509066)|(509047)|(509042)|(509052)|(509043)|(509064)|(509040))\d{10}$')
    hiper_pattern = re.compile(r'^((637[0-9]{1})|(638[0-9]{1})|(639[0-9]{1})|(640[0-9]{1})|(41[0-9]{1}[0-9]{1})|(606282\d{10}))$')


    if visa_pattern.match(card_number) is not None:
        return "Visa"
    elif mastercard_pattern.match(card_number) is not None:
        return "Mastercard"
    elif hipercard_pattern.match(card_number) is not None:
        return 'HiperCard'
    elif amex_pattern.match(card_number) is not None:
        return 'America Express'
    elif diners_pattern.match(card_number) is not None:
        return 'Diners Club'
    elif elo_pattern.match(card_number) is not None:
        return 'elo'
    elif hiper_pattern.match(card_number) is not None:
        return 'Hiper'
    else:
        
        return False

visa = "4532698275119469"
mastercard = "5400355094080027"
hipercard = '6062 8265 5230 3745'
americanExpress = '3728 928879 07434'
dinersClub = '3027 776199 1502'
elo = '5041753229491240'
hiper = '6062827557722616'


brand_visa = validate_credit_card_number(visa)
brand_mastercard = validate_credit_card_number(mastercard)
brand_hipercard = validate_credit_card_number(hipercard)
brand_americanExpress = validate_credit_card_number(americanExpress)
brand_dinersClub = validate_credit_card_number(dinersClub)
brand_elo = validate_credit_card_number(elo)
brand_hiper = validate_credit_card_number(hiper)

print('visa:', brand_visa, '| numero:', visa)
print('mastercard:', brand_mastercard, '| numero:', mastercard)
print('hipercard:', brand_hipercard, '| numero:', hipercard)
print('americanExpress:', brand_americanExpress, '| numero:', americanExpress)
print('dinersClub:', brand_dinersClub, '| numero:', dinersClub)
print('elo:', brand_elo, '| numero:', elo)
print('hiper:', brand_hiper, '| numero:', hiper)