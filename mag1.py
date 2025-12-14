# app.py

import streamlit as st

# --- Funkcje Logiki Magazynu ---

def dodaj_towar(lista_magazynu, nazwa_towaru):
    """Zwraca nową listę z dodanym towarem."""
    if nazwa_towaru:
        nowa_lista = lista_magazynu + [nazwa_towaru]
        st.success(f"Dodano: **{nazwa_towaru}**.")
        return nowa_lista
    return lista_magazynu

def usun_towar(lista_magazynu, nazwa_towaru):
    """Zwraca nową listę po usunięciu pierwszego wystąpienia towaru."""
    if nazwa_towaru in lista_magazynu:
        # Tworzymy kopię listy
        nowa_lista = list(lista_magazynu)
        nowa_lista.remove(nazwa_towaru)
        st.warning(f"Usunięto: **{nazwa_towaru}**.")
        return nowa_lista
    else:
        st.error(f"Błąd: Towar **{nazwa_towaru}** nie znaleziono w magazynie.")
        return lista_magazynu


# --- Interfejs Użytkownika Streamlit ---

st.title("📦 Prosty Magazyn Streamlit (Bez Stanu Sesji)")
st.markdown("Aplikacja oparta o listę. Aby dane były trwałe, **musisz za każdym razem wkleić aktualny stan magazynu**.")

# 1. Wejście: Aktualny Stan Magazynu (Wprowadzany przez Użytkownika)
st.header("1. Aktualny stan magazynu (lista oddzielona przecinkami)")
magazyn_input_str = st.text_area(
    "Wklej obecną listę towarów (np. Krzesło, Stół, Lampa)",
    value=""
)
# Przekształcenie ciągu znaków na listę
magazyn_lista = [item.strip() for item in magazyn_input_str.split(',') if item.strip()]

st.info(f"Obecnie w pamięci: {magazyn_lista}")


# 2. Dodawanie Towaru
st.header("2. Dodaj Nowy Towar")
with st.form("form_dodawanie"):
    nowy_towar = st.text_input("Nazwa Towaru do dodania:").strip()
    przycisk_dodaj = st.form_submit_button("Dodaj i Pokaż Nowy Stan")

    if przycisk_dodaj:
        nowy_magazyn = dodaj_towar(magazyn_lista, nowy_towar)


# 3. Usuwanie Towaru
st.header("3. Usuń Towar")
with st.form("form_usuwanie"):
    towar_do_usuniecia = st.text_input("Nazwa Towaru do usunięcia:").strip()
    przycisk_usun = st.form_submit_button("Usuń i Pokaż Nowy Stan")

    if przycisk_usun:
        nowy_magazyn = usun_towar(magazyn_lista, towar_do_usuniecia)


# 4. Wynik Działania
st.header("4. Wynik (Nowy Stan Magazynu)")

if 'nowy_magazyn' in locals():
    st.code(", ".join(nowy_magazyn))
    st.success(f"Nowa liczba pozycji: **{len(nowy_magazyn)}**")
else:
    st.info("Oczekiwanie na akcję dodania/usunięcia. Pamiętaj, aby skopiować wynik i wkleić go na górze!")
