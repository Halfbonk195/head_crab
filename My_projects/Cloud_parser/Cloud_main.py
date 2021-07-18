import cloud_engine as engine

_login_url = "https://login.1c.ru/login"
_answer_url = 'https://backup.1c.ru/web-api/archives?page=0&size=100'
_del_copy_url = 'https://backup.1c.ru/web-api/archives'
_data = {"inviteCode": '',
         "inviteType": '',
         "username": None,
         "password": None,
         "rememberMe": 'on',
         "execution": 'd37348dc-13d7-4440-ad95-01413a9733dc_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuZUdwbE1XeGhURXN6ZEdWb1VUWjFOWHBXVDBsNGIxQlpXazFpVXpkMk1HWnJZWGhCYlVSamRWVnJTRWhxV1dob1oxbHdTM0JDY1dodlJtdHJVQ3Q0Ym5JelpVUkxOV2xvU21KalNsQnpibXBKU2pSNGQyTldRbWxoZURCa1FsSjVNME4yVlhoNEszUXZPVGh5UlVwRldtbDZTRUZwVkZCSWMwVXZibHBrYkV4b1JVSXJNa1F4U0ZoVWRrZERXRWhDTmtsSGFWUkdTWEZ1WWxWQlJEZElaMnB2Wlc1cFpsbFdjMDg1TURKb1J6bE1WWGQzYTFoUVVUbGFVbTFNZDB0Rk1WaE1SVTVHV1dzNWFrVk1OMWRYYTA5MmRIWXlkWFF6VFhwWlIxZDZUWEJXWjJKdmRVaFROMXA2UkhkS1JWWkliRWt4U1d3MlZITkdSMFZZZWswNE9ESlRNa3RzUjBwT00zcHFhR2xKVUdKdlVrZDBjbGR3YlVWNWVVMTZhVXRVV21kMFkyZEJabFkwUTNSclQybGpTWFpaWlVOUVRpc3ZZMEp2TUZRclVFMTFiRkJaUldNd2FFbHdXRk5pYW1seGJuQk9XVzAwVHpCMFJXZ3lWQ3RsYWpoMU1ETkdXbEJYVWtGUFJVNUtlVE5PY0M4MVR6aHhaRE14Y25jNWJ5OUdVM1J0Um01bmRrbEhOa3RKYWtjd01rVkhhSEJPYmtwWmFVWnRjV3BPVUZWeE5FeFpOM1UxYUV0RVZYVkZRMlJqUTFJM2VWZzRkVk5zU0RBemFIRXZOVzVrUzJ4WGIxVkpaVVpOVUdKNGNTOHpWQzl0ZGpCdGRsQTFLMVIyVTJ4VVoyNXVNRU00TDB4dlJWaHJjMjl3YjFab1dFMDRWVmQxZVZCalR6bEdVR1IwUkZKa2MweFhTbkpPVjBOQ1VuSXlaMms1ZUVGMll6STNORlpPVG1wa1ZVbHNlRXBYTTBaVVJtTm1Sa2sxTjFCMUwzbzBNMlk1VDI5UGJIbHBPQ3R3YUhwMGNETXdUSGxJYjNFeVVGWmxVbUYyU2tGdmFEZFphMjE0ZVRSYVVuVlhRWHB3VmxOaVIyRk9hSGcxTUZSUVdVRnJlblkyV0V0MlRtTnljRkpzWjFaWmFHUjZlbFZoVkN0dFlsWlNOVlZ6Tlc5SE5FVnVibVV4VVUxb01TOWFhVEJtVDB3ckszZGlVbkoxV0RCWFNXTmhRVkIxZVdWUFlWaDZSbGRHYUM5cFJXUkpaMjR3VVhSV1FrZFllSEppWkdoMlIyaFlZVUpuTWpNekt6VmpWMnhEWjFCS1IyZHJkakZEUjFsWVptRkRaREpvTm1GSFZGaDNZMEl6ZGtKU2JXUXJVamhVV1ZSMFVVdGtaSGx4UkdobGJGWXhWa1p4U1U0MlRHWlRlbkZUTTA5aFZrZG5jV2xOUlZGcmJscG9TR1ZLY1c1WFdsaGxja3hEZGpadFVFMDFaV2RxVVVJMU9XZHpTMW8zUkdoVFpFWlJZWGxFTUdWTlNuUlZhVFZQWm1GQmRsZDZNbXhTZUZCeVVFUjBWMnAxWWk5UVUzWkZZMkpOUWxkRVowUmFjak5PUWxoVVNXNHhhbVE1U2l0bGNDOW5hMlpJUW1WSFZYUkhXbXd3VG1NNFNqQlJkbEF4YkZacWFGQjBPRGt2TXpGUEszQnRZVkp1V2tWT1J6ZDBUVzF5WjBOQlFpczFkekJsYkhoWFJ6aEZWM0JhZFVsNWRYQndVakEzYkZoQ1dFZEpjSGxVVVhsbGMxQmpkVFkxY1RGWk1uVkxkM1pwZVVKNFpITktkMHcyWTJ0dVFtSTRiV1l5ZFZBMVptMUhWbWRJUVd4UGRpdE9aVU5OWm5WTWJDc3dlSG8zYWtWek9FUjBkVGgzY1VoM1UwVXJPUzlOVFdOMlIxWkdNMGhPVmpSUEt6VTRTWGg0Y1ZKU1QzVnJUMnBLU3pneGFqaGtRMEZSZUhReWQzb3hRV3RaVEZwamEzVk9RVlJzZFhCR1JHTjRkMGh6TW5OWlFrZHFkVEJHU21kcWJHRjNSSFJJTHpsaFVUUldSRkZWV0hwNlpHbFBSMEp1YWs1dWFYaEtZMjFaYTNkTFRFZElPVUpsU2taV1JuWmhZWHA2T1ZWRlVqWXdaM0ZLVGtkTFlVRnFWR0VyZWtRdlNuY3ZORlJEVkd3NWRXeFROR2x3YzNwaWRXOXpaazVOZEZOeVdsbDNWV2cwZFRGaE9FSjNZVnB6ZFRWcE0yMDJlRzVoYlRCVU5sYzFjbXhNTkRoUkx6RlNVR0YwU1ZOVFdpdE9NMU40TkhFNVFXVnpXQzhyWkM5R1pUWXJOVGhzVjJ4R1RteFlXWG92SzJSVVlUTlRlbkEyWlZabE5IcFpTVmRaUkN0a1kyZHFVekJIVDBGSFlqaDZkMHczZEVacWRsQXJURXB2U1ZKRlVWVnVOMGxyTW5kYVVEUnhRbUZ6TlVwYU5GZDVUUzloY1ZwVk4xZ3hjM1pDUXpodE1uZFBibEJFZG1rNWJIQmxVVmxYU0dGdmRWSkZlR3AwTm5aWE5FbHZibU5LZGtoTlUwRm1iRU01U21SYVZqTjNkbFJIWkVSbk1XczBhbkJNYm5Cc2VXdEphVEV4WmxOSFVXVldSVXBOZFRBNFUwMTJORTVrYm5OTmEwMU5kVTlwZHpCWVprTm1UR05pWms4MU9IQTFlamQ1UzB0dlNFRmpkV2xOYzBWemRIUndMMGRxZGtaU0wzcElMeTlZWTA5WWNsVlVXVkV6VlZnck5Ia3ZXV1l5TlhVd2VtcHRjblJ2UmtveVZFZHVOR2RCTkZreFYyRjJVUzlLYlN0TGVWWTRlRGg2VkVFM01EVnhXak5pZVc5NmVrMDJabEpCU0dwS1REUnRjRmRDUXk5WVYwdGtWV3gzYlhsRE1FUmpieXRMYkVWTVlYQnFaVWxUTkVoTlIyNUdkVGxzU2pCVVFWWnZWSFYxYUVZclJYcGxkWGt6TTFscWRIZDRVRXhWUmtSMGNUUkZVa3ByYmpKdFNYZG9ObmN6U25kMlZXUnlMM0JPT0cxS1JsWkVXRTlNTld4bGVVZEpRM2RPTkdwbGFsaDFRV0Y1WTJwc09XZGlRV1IyTjJOb1MzbE9LMVkzZG1KcVlrUkxOSGw2SzNkS2VYTlplbEJyTjB4eFNteEdZMVZoYWpKNWJFRmFhME5ZTjNKd2VIbHNjM056VW1rd2N6ZFBTRk5ITTAxck4yOTVaRzRyUmpCVlZYQnNjSFZaV25abFYwUlVWek5SWm1kUllWZEhkMUI2VHpSUU0yRnFObXgzUkhOTFZrbzVZbTh6ZFVacWJtbGhZbEJGTkhsVldEWXpVME54TmtSS1NGQm9ORWR5ZGt4NVdGTmxaME5LU2pJM2MybFRhRTB2TDFsNGVUSXhZMWxqVERaNlluTkxiWGhLWXpOcGVYbFVSbUp2TTBKU2FWZ3lXamRtTW1Vd1EwbGFkMFJ6TVVWdVNHcG5TRE52ZGxsSFVEWlRabHAyUkdsT2RFcE9URmhpVGs1SmNIQXlhRmN5UkRjclFrVTRiVFJrYldOamNtVkROalZ2U1RBMU4yYzBkRXR2ZGpOU1ZsRTNPRXhoY1V0VFRqWjFabmR5VjI1aWRsbDJNbWhRUTI5MlFXSlVWRWsxVDFoeVNuY3JlV0ZwZVc1R2FYRmtVWGwzTXl0NVJtZHNWR2RaYUd4S1FtOUNMMkZxVWl0VU1tOUxSaTlZZHpCTWQydHBZVFZFTmtSNmJXa3hUMGRFYkhCVmVYQkRUV04wY2xSRVJGQmtMeTlOVDBKMlQxa3ZNVTlhVVdOa1ZEQTFlRFoxZGpoTVVtRm5Va1ZaYW5sV2VuQlJTRVoxYlU5WGNERXJVbEpNZUhKc2NFNUJha1l6TTFwTk1XOVlhMjFUYVhOWFUwa3JZVWREYVV3NUszWlNaMmRpUjFsVWRXRnFMMkpRYTFnMEwxTnNUVEEwTkUxa09WbFRhRnBzYzNNdmFsRkhlRmxxTUhaeGNFOWpiMVV3WnpkclRsRlNOVTk1WW5aRmJVZGtaVXBoYm5sSmJubE1jVzk0VmpoTFpYaDJNaXR5WVcwd1RUZ3JZVUkyZVhkeU1VWnBNMlJDWWtoWVRUSTBRVzUyVGpoek4wZFlabUZEYUZWT2FtSTFiM1JwZWl0MU5VUXpSSEZCTkhwMlptRjZjRVp6YTA5NlVIQnBURmx5YVRjelNVOUJUbUpXVTFoMVVIVnFabFkzYmtzemNHRnJSRGhaWkRSc1VYbHBNSFJKVDBNMGNVTjBjbEE1Y3pGUFVFbGhNMmxGYXpCcVkxVnNSSEEzVG5aQmRuTkliRFZLYVc5MFNYRXpkbWRKT0RaT2FuSkZhR3RuZGpBMFZHbGxaemw0VkVOcU4waHpjR00zZWk4emF6SllhR1poVEU1R1NFcFpTVzh4YldKTlRFWmxPVVJoZW5wRllYVnNkMk5zZEhSamJHdzBiemd2Wm1jek9FeFRlVUZVZFZwNlQzZFZjbFpxVXpZM2EycG1ObTFWVlZKc1dGTnVNR3hEV0c1WU9FOUJORzVHWVdwMk5sQk9ka1pZVlVKWmVsVm9WRWgyYlV4WU9UTjRLelpGT0dGSVRDOU1RWGwyVkdkd1FVdGlWWEJxTXpjeVdXaERjMVpxTkVORVUwRm1hRzB2T1hBMVJUTkxTRzVST0cxMlEwdFJMMVIxZVRSQ01URkZUM1ZJU1ZCcmEweFJjRFJ1TkRCR1NrZ3hVSFZ5TTFnMlRVaGtNRlphVUU1T1kxRklNRUZ3ZDNGSVNXNHdOa2gzZEhKQlRWUjFNRTlKY0dwcmJWQjZLMU5TWlZkd1dGUTFjVEZuWTFKNVZGcDNTRkpYUVZRNVdVazBNalF2YkdvNE0wSmxkR05QVWxoVVFraHVTME5ZYVVveVYwbExZVmM1YUhGaWNWWmxiM0Z0ZURSclkwcEJTMUp3YjNaSWJrVkhOR05IVEZGVlpEaHZTRmQ2ZEVORVpWbEZiV3BxZFRjMWMyVldhbXBPYVhGSlRtTjVlU3Q0UkVSUFZVc3lUMDFtY0RSeWJHeHVReXMzTXpGV1NHRjZkakJrV0ZOTE9VRlBiREJ0VFRkUVp6bGlNMUZNUlVKaVNHaG5iSEJDTTBoMk1WUXpVMFF4T1RKYVZraExhMGhXYTFnNVFVc3JUQzltSzNkdlUyRnlTUzlOWjNsVmN6ZENjRnA0Um1ORFpFcHJWbnBuV0dWTmVsUkpOa2hQV0ZvemIwZFVZVGQwU3pkSlQwazVhVEJVTWpWSk1tRnpZaTh4T0UxWlFtOXFXbFp5WjB4TlMwdHBUMFV2T0ZCQ2NXMUVVMlZEUTJFdk1GQm9lVGR2SzJRclVURm9OakI1V21ObFNrZFdUVE5wYUdkTlRsbExUWE5aTjNsUFdqZHRhMVppWkhkU0sxZGtTMFJ0WjFJMFUwdzJZakZEV0RoVWMyRllSWEoyVjI5eFJUVjFSak54YkZWT1YwdGxWa0ZyVWpsT2JrSXZOM2RxV0RsRlFuY3diMVpCU2tzd2JERmlUblpNU2t3Mk1GQmtkRmRQT1hFNWQwWlBVV3hpV1VSak1URmxSblpGVkRsTldEVmFja2RLVkVSaWVsSjZhMDFDYW1Kc05ITjNZMnhYYW5BdmJXdGhkR3hyTUdOdVUyWkdNbVJwZFd0bmRURlJOamhvYkhsU2FHNUtlWFp0Vm1aNVF6QktSVEZ5V0dwUlVrVXZlRWRzYUVGT0t6SjBObmhzYUd3MFFYUkxlWFZFZDBwWlQzRlNaM1JhYzFGUlFXSmxVR3hKV1V0YVZtbGhiVFYzV2sxWlRFczRTMkpWYlZKT1YzWlNkR3hXY0VoaVVtaHlVR2hNYm1KVlIzUndaVkV4Ym14S01td3lUV05tYmtaTlVFOUJibVI0Ym1KNWNsRm1iM2RHTWpab2JXeDRWWFZYYTNCd05tRXJXRk4zYTJsalZscG5hM2xzVVU1a2RFeEpWbXB3V2xVdk1rdFdXbXRPUjJob1JWbHlibEJSYW5ad2RtRlFUMVZYT0ZWVllrTXplVzVCZFVNMWQzVk5QUS5nNjhQYTdUd05SQWt6d1hSYzFnY0FJNDVRUHZzb0g4NV9ibi1ReWZxTkE4dElNX1FiTmRtSnVpZ0VNajZQR2EzbjBHZnNtV052Sm9idlFkVllZYXBQUQ==',
         "_eventId": 'submit',
         "geolocation": '',
         "submit": 'Войти'}


def spliter(date, name, bd_id):
    split_date = date.split(':')
    split_date = split_date[1][1:11]
    split_date = split_date.split('-')
    split_date = split_date[2] + '.' + split_date[1] + '.' + split_date[0]

    split_name = name.split(':')
    split_name = split_name[1][1:] + split_name[2][:-1]

    bd_id = bd_id.split(',')
    bd_id = bd_id[0].split(':')
    bd_id = bd_id[-1]

    return split_date, split_name, bd_id[1:-1]


def del_copy(bd_id):
    while True:
        count_copy = input('Введите количество копий, которые вы хотите удалить (удаляются начиная с конца):')

        if not count_copy.isnumeric():
            print('Ты что издеваешься, введи, пожалуйста цифру - попробуй еще раз!\n')
            continue

        count_copy = int(count_copy)
        if count_copy == 0 or count_copy >= len(bd_id):
            print('Вы ввели неверное количество копий, попробуйте еще раз!\n')
            continue

        else:
            temp_list_bd_id = []
            j = 0
            while j < count_copy:
                temp_list_bd_id.append(bd_id[len(bd_id) - 1 - j])
                j += 1
            data_put = {'ids': temp_list_bd_id}
            loginbot.put(_del_copy_url, data=data_put)
            print(f'Успешно удалено {count_copy} старых копий!')
            break


print("*****Вас приветствует Cloud parser v1.01, которая покажет Вам все копии в ОА и их дату создания*****")
print("Все права защищены Антипин Т.В.")
print("Введите логин и пароль от portal.1c.ru:")


def main_method():
    if _login_url in answer:
        print("Вы ввели неверный логин или пароль, попробуйте еще раз...")
    else:
        split_answer = answer.split(',')
        dates_bd = [el for el in split_answer if "timeConfigDate" in el]
        names_bd = [el for el in split_answer if "ibPath" in el]
        id_bd_list = [el for el in split_answer if "id" in el]

        if len(dates_bd) != 0:
            len_bd = 0
            i = 0
            bd_id = []
            bd_names = []

            for elems in dates_bd:
                date, name, bd_id_tmp = spliter(elems, names_bd[i], id_bd_list[i])
                bd_id.append(bd_id_tmp)
                bd_names.append([name, date])

                if len(name) > len_bd:
                    len_bd = len(name)
                i += 1
            print_table(bd_names, len_bd)

            total_space = loginbot.parser('https://backup.1c.ru/web-api/space')
            total_space = total_space.split(',')
            for elems in total_space:
                new_elems = elems.split(':')
                total_space[total_space.index(elems)] = new_elems[1]

            print(f'\nИспользовано: {total_space[0]} МБ, Всего: {total_space[1][:-1]} ГБ\n')

            if int(total_space[0][:-2]) > 15000:
                print('Может пора почистить копии? ******БУДЬ ОСТОРОЖЕН******')

            usr_answer = input('Если хотите удалить копии введите yes (если не хотите, введите любой другой символ):')
            if usr_answer.lower() == 'yes':
                del_copy(bd_id)
        else:
            print("Нет копий!")


def print_table(bd_names, len_bd):
    massage_1 = 'Расположение базы'
    massage_2 = 'Дата создания'
    massage_3 = '|' + '-' * (len_bd + 2) + '|' + '-' * 15 + '|'
    print(f'\n| {massage_1:^{len_bd + 1}}|{massage_2:^15}|')
    print(massage_3)
    for items in bd_names:
        print(f'| {items[0]:<{len_bd + 1}}|{items[1]:^15}|')


while True:
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    _data['username'] = login
    _data['password'] = password
    loginbot = engine.Loginbot(_data, _login_url)
    answer = loginbot.parser(_answer_url)

    try:
        main_method()
    except IndexError as ecx:
        print("Нет копий!")

    end = input("\nВведите 'q' для выхода, любую другую клавишу для продолжения ")
    if "q" == end.lower() or "й" == end.lower():
        break
    print('--------------------------------------------------')
