{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "# TD : Listes en python "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "## Exercice 1 : Insertion dans un tableau"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "Définir une fonction `insertion_tableau` prenant en paramètre une liste `L`, une valeur `v` et un indice `i` et insérant la valeur `v` à l'indice `i` dans `L` (fonction comparable à `L.insert(i,v)` définie en Python). \n",
    "\n",
    "Cette fonction ne doit pas utiliser la fonction `L.insert`, seule la fonction  `L.append` est permise pour augmenter la taille du tableau."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "Quelle est la complexité asymptotique de la fonction `insertion_tableau` ?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "run_control": {
     "frozen": false
    },
    "tags": [
     "answer"
    ]
   },
   "source": [
    "**Réponse :** Écrire votre réponse ici.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "## Exercice 2 : suppression d'un élément dans un tableau\n",
    "\n",
    "Définir la fonction `suppression_tableau` prenant en paramètre un tableau et un indice et supprimant dans le tableau l'élément se trouvant à l'indice donné (fonction similaire à `L.pop(i)`). \n",
    "\n",
    "Pour supprimer un élément, la fonction peut juste appeler la fonction `L.pop()` (sans argument) pour supprimer la dernière case."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "Quelle est la complexité de la fonction `suppression_tableau` ?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "run_control": {
     "frozen": false
    },
    "tags": [
     "answer"
    ]
   },
   "source": [
    "**Réponse :** Écrire votre réponse ici.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "## Exercice 3 : Copie d'un tableau"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "Définir la fonction `copie_tableau` retournant une copie du tableau `L` passé en paramètre (fonction comparable à `L.copy()`). \n",
    "\n",
    "Cette fonction ne doit pas utiliser la fonction `L.copy`, seule la fonction `L.append` est permise pour augmenter la taille du tableau."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "Quelle est la complexité asymptotique de la fonction `copie_tableau` ?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "run_control": {
     "frozen": false
    },
    "tags": [
     "answer"
    ]
   },
   "source": [
    "**Réponse :** Écrire votre réponse ici.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "## Exercice 4 : Fonctions sur des  listes (tableaux) triées ou non triées"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "Les questions de cet exercice ont pour objet de manipuler les listes/tableaux en Python et de comparer ce qui se passe si on travaille avec des tableaux triés ou des tableaux quelconques. Pour chacune des fonctions à implémenter, on définira deux versions : \n",
    "\n",
    "* une première version prendra en paramètre une liste de nombres quelconques. Pour plus d'efficacité, la fonction pourra modifier l'ordre des éléments dans la liste,\n",
    "\n",
    "* la seconde version prendra en paramètre une liste de nombres triés dans l'ordre croissant ; la liste devra rester triée."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "### Question 1 : Minimum d'un tableau"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "* Définir la fonction `minimum_tableau` prenant en paramètre un tableau de nombres et retournant le minimum."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "* Définir la fonction `minimum_tableau_trie` prenant en paramètre un tableau de nombres triés dans l'ordre croissant et retournant le minimum."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "- Quelle est la complexité dans le pire des cas de chacune de ces fonctions ?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "run_control": {
     "frozen": false
    },
    "tags": [
     "answer"
    ]
   },
   "source": [
    "**Réponse :** Écrire votre réponse ici.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "### Question 2 : Ajout d'un élément"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "* Définir la fonction `ajouter_tableau` ajoutant un nombre à un tableau de nombres."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "* Définir la fonction `ajouter_tableau_trie` ajoutant un nombre à un tableau trié."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "- Quelle est la complexité dans le pire des cas de chacune de ces fonctions ?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "run_control": {
     "frozen": false
    },
    "tags": [
     "answer"
    ]
   },
   "source": [
    "**Réponse :** Écrire votre réponse ici.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "### Question 3 : Suppression d'un élément"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "* Définir la fonction `supprimer_tableau` prenant en paramètre un tableau et un indice `id` et supprimant dans le tableau la valeur d'indice `id`.\n",
    "\n",
    "  On utilisera pour cela la fonction `L.pop()` qui supprime la dernière case d'un tableau, mais pas la fonction `L.pop(i)`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "* Définir la fonction `supprimer_tableau_trie` prenant en paramètre un tableau trié et un indice `id` et supprimant dans le tableau la valeur d'indice `id`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "- Quelle est la complexité dans le pire des cas de chacune de ces fonctions ?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "run_control": {
     "frozen": false
    },
    "tags": [
     "answer"
    ]
   },
   "source": [
    "**Réponse :** Écrire votre réponse ici.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "## Exercice 5 : Réarrangement de tableau**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "### Question 1\n",
    "\n",
    "Écrire une fonction `deplacer(T, k)` prenant en paramètre un tableau `T` et une valeur `k` et permutant les valeurs du tableau `T` de manière à ce que toutes les valeurs strictement inférieures à `k` soient au début de tableau. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "**Remarque :** L'ordre des éléments dans le tableau n'a pas d'importance tant que les éléments strictement inférieurs à `k` sont placés au début du tableau."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    }
   },
   "source": [
    "### Question 2\n",
    "\n",
    "Définir une fonction de tests unitaires de la fonction `deplacer`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "answer"
    ]
   },
   "outputs": [],
   "source": [
    "############################## \n",
    "#   Saisir votre code ici.   #\n",
    "##############################\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Format de la Cellule Texte Brut",
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": false,
   "sideBar": false,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": false,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}