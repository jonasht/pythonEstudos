
import re

def validate_credit_card_number(card_number):
    visa_pattern = re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$')
    mastercard_pattern = re.compile(r'^5[1-5][0-9]{14}$')
    hipercard_pattern = re.compile(r'^(606282\d{10}(\d{3})?)|(3841\d{15})$')
    amex_pattern = re.compile(r'^3[47][0-9]{13}$')
    diners_pattern = re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$')
    elo_pattern = re.compile(r'^((636368)|(438935)|(504175)|(451416)|(509048)|(509067)|(509049)|(509069)|(509050)|(509074)|(509068)|(509040)|(509045)|(509051)|(509046)|(509066)|(509047)|(509042)|(509052)|(509043)|(509064)|(509040))\d{10}$')
    cabal_pattern = re.compile(r'^((6042)[\d]{12})|((5896)[\d]{13})$')
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
    elif cabal_pattern.match(card_number) is not None:
        return 'Cabal'
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
cabal = '6271-1134-0943-9288'
hiper = '6062827557722616'


brand_visa =
brand_mastercard =
brand_hipercard =
brand_americanExpress =
brand_dinersClub =
brand_elo =
brand_cabal =
brand_hiper =