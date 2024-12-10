{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "62290144",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "import sys\n",
    "import csv\n",
    "\n",
    "for line in sys.stdin:\n",
    "    # Supprimer les espaces inutiles\n",
    "    line = line.strip()\n",
    "\n",
    "    # Lire les lignes CSV\n",
    "    reader = csv.reader([line])\n",
    "    for row in reader:\n",
    "        if len(row) == 7:  # Vérifier que toutes les colonnes sont présentes\n",
    "            try:\n",
    "                product = row[1]\n",
    "                quantity = float(row[2])\n",
    "                price = float(row[3])\n",
    "                address = row[5]\n",
    "                month = row[6]\n",
    "\n",
    "                # Calculer les ventes totales\n",
    "                total_sales = quantity * price\n",
    "\n",
    "                # Extraire la région (état) de l'adresse\n",
    "                region = address.split(\",\")[-1].split()[0]  # Extrait \"TX\", \"MA\", etc.\n",
    "\n",
    "                # Émettre une clé combinée : (Produit, Région, Mois)\n",
    "                print(f\"{product},{region},{month}\\t{total_sales}\")\n",
    "            except ValueError:\n",
    "                # Ignorer les lignes mal formées\n",
    "                continue\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df85697d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
