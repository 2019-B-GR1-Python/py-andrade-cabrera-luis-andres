import CRUD_manager
import viewModel

creditos = """====================================================================================================================================
                     +oyhhhhhhhso          `:/ooo+/-`              +oyhhhhhhhso          .:+ooo+/-
                        yMMMMM:         -smMMdsooymMMd+`              yMMMMM:         -ymMMMMMMMMMMh+`
                        oMMMMM`       .hMMMs`      :dMMNo`            oMMMMM        -dMMMhoyMMMN/smMMN+
                        oMMMMM`      /MMMM/         `hMMMm.           oMMMMM       +MMMN/:+NMmMMs::dMMMd`
                        oMMMMM`     :MMMMy           `NMMMm`          oMMMMM      /MMm/yMMMMm.oMMMMm+yMMd
                        oMMMMM`     mMMMM-            sMMMMo          oMMMMM      NMMMh `-+syNhso:. /MMMM/
                        oMMMMM`    .MMMMM             /MMMMd          oMMMMM     :MMNm+    :hMm+`   .hNMMy
                        oMMMMM`    -MMMMN             :MMMMd          oMMMMM     :MMo   `sNMMMMMMh:   .MMh
                        oMMMMM`    `MMMMM`            +MMMMy          oMMMMM     .MMNd/ mMMMMMMMMMM-.hmMMo
                        oMMMMM`     sMMMM+            dMMMM-          oMMMMM      yMMM+ oMMMyh+NMMd`.mMMN`
                 .-`    oMMMMM`      hMMMN`          +MMMM/    .-`    oMMMMM      `dMMs` `.` y  ..  /NMM:
                hMMM/   oMMMMN        sMMMm-        +MMMN:   `dMMM/   oMMMMN       `yMMNdMN: y  dMNdMMm-
               .MMMM/   oMMMMo         .yNMMy/.``-+mMMm+`    -MMMM/   oMMMMo         -yMMMMmhmyhMMMMd+
                yMMy    dMMMs            `:ohdmNNmdy+-        yMMs    dMMMs            `:ohmmNNmdy+.
                 -sdhssmNds.                                   -sdhssmNdo.
                   ```                                           ``
===================================================================================================================================="""

menu = """Bienvenido a la Jojo's Stand Dex
1 - Insertar
2 - Mostrar
3 - Actualizar
4 - Eliminar
5 - Salir
"""

sub_menu_types = """Elija el tipo
1 - Stand Master
2 - Stand
3 - Regresar
"""

def show_menu():
    eleccion = None
    while eleccion is not 5:
        viewModel.clear()
        print(creditos)
        print(menu)
        eleccion = int(input("Elige: "))
        if eleccion is 1:
            print(sub_menu_types)
            tipo_eleccion = int(input("Elige: "))
            if tipo_eleccion is 1:
                viewModel.create_new_user()
            elif tipo_eleccion is 2:
                viewModel.create_new_stand()
            input()
        elif eleccion is 2:
            print(sub_menu_types)
            tipo_eleccion = int(input("Elige: "))
            if tipo_eleccion is 1:
                viewModel.show_all_users()
            elif tipo_eleccion is 2:
                viewModel.show_all_stands()
            input()
        elif eleccion is 3:
            print(sub_menu_types)
            tipo_eleccion = int(input("Elige: "))
            if tipo_eleccion is 1:
                viewModel.update_user(viewModel.select_item_id("users.csv"))
            elif tipo_eleccion is 2:
                viewModel.update_stand(viewModel.select_item_id("stands.csv"))
            input()
        elif eleccion is 4:
            print(sub_menu_types)
            tipo_eleccion = int(input("Elige: "))
            if tipo_eleccion is 1:
                viewModel.delete_user(viewModel.select_item_id("users.csv"))
                viewModel.show_all_users()
            elif tipo_eleccion is 2:
                viewModel.delete_stand(viewModel.select_item_id("stands.csv"))
                viewModel.show_all_stands()
            input()
