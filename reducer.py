{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b3880a32",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "import sys\n",
    "\n",
    "current_key = None\n",
    "current_total = 0.0\n",
    "\n",
    "for line in sys.stdin:\n",
    "    # Supprimer les espaces inutiles\n",
    "    line = line.strip()\n",
    "\n",
    "    # Découper la ligne en clé et valeur\n",
    "    key, value = line.split(\"\\t\")\n",
    "    value = float(value)\n",
    "\n",
    "    # Agréger les ventes pour chaque clé\n",
    "    if current_key == key:\n",
    "        current_total += value\n",
    "    else:\n",
    "        if current_key:\n",
    "            # Écrire le total pour la clé précédente\n",
    "            print(f\"{current_key}\\t{current_total}\")\n",
    "        current_key = key\n",
    "        current_total = value\n",
    "\n",
    "# Écrire le dernier total\n",
    "if current_key:\n",
    "    print(f\"{current_key}\\t{current_total}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "242688a7",
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
