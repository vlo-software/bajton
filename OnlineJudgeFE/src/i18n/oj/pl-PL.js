export const m = {
  // 404.vue
  Go_Home: 'Wróć na stronę główną',
  // Problem.vue
  Description: 'Opis',
  Input: 'Wejście',
  Output: 'Wyjście',
  Sample_Input: 'Przykładowe wejście',
  Sample_Output: 'Przykładowe wyjście',
  Hint: 'Wskazówka',
  Source: 'Źródło',
  Status: 'Status',
  Information: 'Informacje',
  Time_Limit: 'Limit czasowy',
  Memory_Limit: 'Limit pamięci',
  Created: 'Autor',
  Level: 'Poziom',
  Score: 'Wynik',
  Tags: 'Tagi',
  Show: 'Pokaż',
  Submit: 'Wyślij',
  Submitting: 'Wysyłanie',
  Judging: 'Ocenianie',
  Wrong_Answer: 'Zła odpowiedź',
  Statistic: 'Statystyki',
  Close: 'Zamknij',
  View_Contest: 'Pokaż konkurs',
  Are_you_sure_you_want_to_reset_your_code:
    'Czy napewno chcesz usunąć swój kod?',
  Code_can_not_be_empty: 'Kod nie może być pusty.',
  Submit_code_successfully: 'Wysyłanie kodu powiodło się',
  You_have_solved_the_problem: 'Problem jest już przez ciebie rozwiązany',
  Submitted_successfully: 'Wysłano z powodzeniem',
  You_have_submitted_a_solution: 'Rozwiązanie zostało przez ciebie wysłane.',
  Contest_has_ended: 'Konkurs się skończył',
  You_have_submission_in_this_problem_sure_to_cover_it:
    'Masz już rozwiązanie tego problemu, czy napewno chcesz je zastąpić?',
  // About.vue
  Compiler: 'Kompilator',
  Result_Explanation: 'Wyjaśnienie wyniku',
  Pending_Judging_Description:
    'Twoje rozwiązanie zostanie niedługo ocenione, zaczekaj na wynik.',
  Compile_Error_Description:
    'Twój kod się nie skompilował. Kliknij na link aby zobaczyć output kompilatora.',
  Accepted_Description: 'Gratulacje. Twoje rozwiązanie jest poprawne.',
  Wrong_Answer_Description:
    'Wyjście twojego programu nie zgadza się z odpowiedzią sędziego.',
  Runtime_Error_Description:
    'Twój program wyszedł w sposób nadzwyczajny. Możliwe przyczyny: segment fault, dzielenie przez zero lub exit code inny niż 0.',
  Time_Limit_Exceeded_Description:
    'Twój program przekroczył limit czasu procesora.',
  Memory_Limit_Exceeded_Description: 'Twój program przekroczył limit pamięci.',
  System_Error_Description:
    'Ups, sędzia spadł z rowerka. Proszę poimformuj o tym administratora.',
  // ACMContestRank.vue
  Menu: 'Menu',
  Chart: 'Wykres',
  Auto_Refresh: 'Automatyczne odświeżanie',
  RealName: 'Prawdziwa nazwa',
  Force_Update: 'Wymuś aktualizację',
  download_csv: 'pobierz csv',
  TotalTime: 'Całkowity czas',
  Top_10_Teams: 'Top 10 zespołów',
  save_as_image: 'zapisz jako zdjęcie',
  // ACMHelper.vue
  ACM_Helper: 'Pomocnik ACM',
  AC_Time: 'Czas AC',
  ProblemID: 'ProblemID',
  First_Blood: 'First Blood',
  Username: 'Nazwa użytkownika',
  Checked: 'Sprawdzone',
  Not_Checked: 'Nie sprawdzone',
  Check_It: 'Sprawdź',
  // ACMRank.vue
  ACM_Ranklist: 'ACM Ranklist',
  mood: 'nastrój',
  AC: 'AC',
  Rating: 'Ocena',
  // Announcements.vue
  Contest_Announcements: 'Ogłoszenia konkursowe',
  By: 'Autor',
  // ApplyResetPassword.vue
  The_email_doesnt_exist: 'Email nie istnieje',
  Success: 'Sukces',
  Password_reset_mail_sent:
    'Email do przywrócenia pasła został do ciebie wysłany.',
  // FAQ.vue
  Frequently_Asked_Questions: 'Często zadawane pytania',
  Where_is_the_input_and_the_output: 'Gdzie jest wejście i wyjście?',
  Where_is_the_input_and_the_output_answer_part_1:
    'Twój program powinnien wczytać wejście z',
  Standard_Input: 'Standard Input',
  Where_is_the_input_and_the_output_answer_part_3: 'i zapisać wyjście do',
  Standard_Output: 'Standard Output',
  Where_is_the_input_and_the_output_answer_part_5: 'Na przykład, możesz użyć',
  Where_is_the_input_and_the_output_answer_part_6: 'w C lub',
  Where_is_the_input_and_the_output_answer_part_7:
    'w C++ aby wczytać z stdin, oraz',
  Where_is_the_input_and_the_output_answer_part_8: 'w C lub',
  Where_is_the_input_and_the_output_answer_part_9:
    'w C++ aby zapisać do stdout.  Programy użytkowników nie mogą czytać, ani zapisywać plików, albo dostaniesz',
  What_is_the_meaning_of_submission_execution_time:
    'Jakie jest znaczenie czasu wykonywania rozwiąznia?',
  What_is_the_meaning_of_submission_execution_time_answer:
    'SędziaOnline może testować twój kod wielokrotnie, z różnymi wejściami. Jeśli twój kod zwróci poprwaną odpowiedź, mieszcząc się w limicie czasowym dla każdego pliku wejściowego, wyświetlony czas wykonywania to maksymalny czas spędzony na wykonywaniu każdego przypadku testowego. W przeciwnym wypadku, czas wykonywania nie będzie miał sensu.',
  How_Can_I_use_CPP_Int64: 'Jak mogę użyć C++ Int64?',
  How_Can_I_use_CPP_Int64_answer_part_1: 'Musisz zadeklarować jako',
  How_Can_I_use_CPP_Int64_answer_part_2: 'i użyć z',
  or: 'lub',
  using: 'użycie',
  How_Can_I_use_CPP_Int64_answer_part_3: 'zaowocuje w',
  Java_specifications: 'Specyfikacja Java?',
  Java_specifications_answer_part_1:
    'Wszystkie programy muszą zaczynać się od metody static main w',
  Java_specifications_answer_part_2:
    'klasie. Nie używaj klas publicznych: nawet',
  Java_specifications_answer_part_3:
    'musi być niepubliczne aby uniknąć błędu kompilacji. Używaj buffered I/O aby uniknąć przekroczenia czasu procesora, przez nadmierne czyszczenie strumienia.',
  About_presentation_error: 'Co z błędem przezntacji?',
  About_presentation_error_answer_part_1:
    'Nie ma tu błędu przezntacji. Sędzia obetnie zawinięcia w twojego wyjścia',
  last: 'ostatniej',
  About_presentation_error_answer_part_2:
    'lini.  Jeśli wynik dalej się nie zgadza, zwrócony zostanie',
  How_to_report_bugs: 'Jak zgłaszać bugi?',
  How_to_report_bugs_answer_part_1:
    'Onlinejudge jest open source, możesz stworzyć issue na',
  How_to_report_bugs_answer_part_2:
    'Szczegóły (jak env, wersja..) na temat buga są wymagane, pomogą rozwiązać twój problem. Ta wersja Onlinejudge jest zmodyfikowna na potrzeby V Liceum w Gdańsku, więc lekko odbiega od kodu dostępnego w oficjalnym repozytorium.',
  // Cancel.vue
  Cancel: 'Anuluj',
  // ContestDetail.vue
  Problems: 'Problemy',
  Announcements: 'Ogłoszenia',
  Submissions: 'Rozwiązania',
  Rankings: 'Rankingi',
  Overview: 'Przegląd',
  Admin_Helper: 'Pomocnik administratora',
  StartAt: 'Rozpoczęcia o',
  EndAt: 'Zakończenie o',
  ContestType: 'Rodzaj konkursu',
  Creator: 'Twórca',
  Public: 'Publiczne',
  Password_Protected: 'Zabezpieczone pasłem',
  // ContestList.vue
  Rule: 'Zasada',
  OI: 'OI',
  ACM: 'ACM',
  Underway: 'W trakcie',
  Not_Started: 'Nie rozpoczęty',
  Ended: 'Zakończony',
  No_contest: 'Brak konkursu',
  Please_login_first: 'Najpierw się zaloguj!',
  // ContestProblemList
  Problems_List: 'Lista problemów',
  No_Problems: 'Brak konkursów',
  // CodeMirror.vue
  Language: 'Język',
  Theme: 'Wygląd',
  Reset_to_default_code_definition: 'Przywróć do domyślnej definicji kodu',
  Upload_file: 'Wgraj plik',
  Toggle_vim: 'Przełącz tryb Vim',
  Vim_enabled: 'Key bindingi Vim zostały włączone.',
  Sublime_enabled: 'Key bindingi Sublime zostały włączone.',
  Are_you_sure_you_want_to_enable_vim:
    'Czy napewno chcesz włączyć key bindingi Vim?<br/><br/><em>Raczej nie chcesz.</em><br/><br/>Jeśli klikniesz ok i utkniesz, możesz zawsze wrócić do key bindingów sublime, klikając ponownie na przycisk Vim.',
  Monokai: 'Monokai',
  Solarized_Light: 'Solarized Light',
  Material: 'Material',
  // KatexEditor.vue
  Latex_Editor: 'Edytor Latex',
  // NavBar.vue
  Home: 'Dom',
  NavProblems: 'Problemy',
  Contests: 'Konkursy',
  NavStatus: 'Status',
  Rank: 'Ranking',
  ACM_Rank: 'Ranking ACM',
  OI_Rank: 'Ranking OI',
  About: 'Informacje',
  Judger: 'Sędzia',
  FAQ: 'FAQ',
  Login: 'Zaloguj się',
  Register: 'Zarejestruj się',
  MyHome: 'Dom',
  MySubmissions: 'Rozwiązania',
  Settings: 'Ustawienia',
  Management: 'Zarządzanie',
  Logout: 'Wyloguj',
  Welcome_to: 'Witaj w',
  // announcements.vue
  Refresh: 'Odśwież',
  Back: 'Wróć',
  No_Announcements: 'Brak ogłoszeń',
  // Setting.vue
  Profile: 'Profil',
  Account: 'Konto',
  Security: 'Bezpieczeństwo',
  // AccoutSetting.vue
  ChangePassword: 'Zmień pasło',
  ChangeEmail: 'Zmień email',
  Update_Password: 'Zaktualizuj pasło',
  // ProfileSetting.vue
  Avatar_Setting: 'Ustawienia avatara',
  Profile_Setting: 'Ustawienia profilu',
  // SecuritySettig
  Sessions: 'Sesje',
  Two_Factor_Authentication: 'Two Factor Authentication',
  // Login.vue
  LoginUsername: 'Nazwa użytkownika',
  LoginPassword: 'Pasło',
  TFA_Code: 'Kod z twojej aplikacji TFA',
  No_Account: 'Nie masz konta? Zarejestruj się teraz!',
  Forget_Password: 'Nie pamiętasz pasła?',
  UserLogin: 'Zaloguj się',
  Welcome_back: 'Witaj z powrotem w OJ',
  // OIRank.vue
  OI_Ranklist: 'Lista rankingowa OI',
  // OIContestRank.vue
  Total_Score: 'Łączny wynik',
  // ProblemList.vue
  Problem_List: 'Lista problemów',
  High: 'Wysoki',
  Mid: 'Średni',
  Low: 'Niski',
  All: 'All',
  Reset: 'Resetuj',
  Pick_One: 'Wybierz jeden',
  Difficulty: 'Trudność',
  Total: 'Razem',
  AC_Rate: 'AC Rate',
  // Register.vue
  RegisterUsername: 'Nazwa użytkownika',
  Email_Address: 'Adres email',
  RegisterPassword: 'Pasło',
  Password_Again: 'Znowu pasło',
  Captcha: 'Captcha',
  UserRegister: 'Zarejestruj',
  Already_Registed: 'Już masz konto? Zaloguj się teraz!',
  The_username_already_exists: 'Nazwa użytkownika jest już zajęta.',
  The_email_already_exists: 'Adres email jest już zajęty',
  password_does_not_match: 'pasło się nie zgadza',
  Thanks_for_registering:
    'Dziękujemy za rejestrację, możesz się teraz zalogować!',
  // ResetPassword.vue and ApplyResetPassword.vue
  Reset_Password: 'Zgubione pasło',
  RPassword: 'Pasło',
  RPassword_Again: 'Znowu pasło',
  RCaptcha: 'Captcha',
  ApplyEmail: 'Twój adres email',
  Send_Password_Reset_Email: 'Wyślij maila do przywrócania pasła ponownie',
  Your_password_has_been_reset: 'Twoje pasło zostało przywrócone.',
  // Save.vue
  Save: 'Zapisz',
  // Simditor.vue
  Uploading_is_in_progress:
    'Wgrywanie w toku, czy napewno chcesz opuścić tą stronę?',
  // SubmissionDetails.vue
  Lang: 'Język',
  Share: 'Udostępnij',
  UnShare: 'Odudostępnij',
  Succeeded: 'Udało się',
  Real_Time: 'Czas rzeczywisty',
  Signal: 'Signal',
  // SubmissionList.vue
  When: 'Kiedy',
  ID: 'ID',
  Time: 'Czas procesora',
  Memory: 'Pamięć',
  Author: 'Autor',
  Option: 'Opcja',
  Mine: 'Moje',
  Search_Author: 'Szukaj autora',
  Accepted: 'Zaakceptowane',
  Time_Limit_Exceeded: 'Limit czasu przekroczony',
  Memory_Limit_Exceeded: 'Limit pamięci przekroczony',
  Runtime_Error: 'Runtime Error',
  System_Error: 'System Error',
  Pending: 'W trakcie',
  Partial_Accepted: 'Częściowo zaakceptowane',
  Compile_Error: 'Błąd kompilacji',
  Rejudge: 'Sprawdź ponownie',
  // UserHome.vue
  UserHomeSolved: 'Rozwiązane',
  UserHomeserSubmissions: 'Rozwiązania',
  UserHomeScore: 'Wynik',
  List_Solved_Problems: 'Lista rozwiązanych problemów',
  UserHomeIntro:
    'Ta osoba jest tak leniwa, że nie rozwiązała jeszcze żadnych problemów.',
  // TODO: move this
  Details: 'Więcej',
  Submission_Outputs: 'Wyjścia',
  Submission_Output_Test: 'Wyjście testu:',
  Submission_Output_SubmissionOutput: 'Wyjście programu:',
  Submission_Tests: 'Wyniki testów',
  Submission_Code: 'Kod'
}
