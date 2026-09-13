"""REFEREE turn 618, part 3: calibration of the two instruments used in parts
1 and 2, against figures the ledger already carries.

Run:  python3 referee_t618_checks3.py
"""
from kobon import corpus, table
from referee_t618_checks2 import hb_cyclic, total_parity

C = corpus.by_key()

print("=" * 72)
print("parity checker, against reference data 46e's published calibration")
for key in ("kobon_8", "kobon_13_m_sym_47tri", "kobon_14_53tri",
            "kobon_17_85tri", "kobon_18_93tri", "kobon_20_116tri"):
    t = C[key]["table"]
    print("   %-22s naive %3d of %5d   (table.count %d)"
          % (key, *total_parity(t), table.count(t)))

print()
print("=" * 72)
print("happens-before checker, against reference data 46e")
B = C["kobon_13_m_sym_47tri"]["table"]


def b_plus_14(row14, slots):
    t = [list(r) for r in B]
    for i, s in slots.items():
        if s == 'front':
            t[i - 1] = [14] + t[i - 1]
        elif s == 'back':
            t[i - 1] = t[i - 1] + [14]
        else:
            t[i - 1] = t[i - 1][:s] + [14] + t[i - 1][s:]
    t.append(list(row14))
    return t


for key in ("kobon_13_m_sym_47tri", "kobon_14_53tri", "kobon_18_93tri",
            "kobon_20_116tri", "kobon_8"):
    cyc, nn, un = hb_cyclic(C[key]["table"])
    print("   %-22s %s, %d nodes, %d unresolved"
          % (key, "CYCLIC" if cyc else "acyclic", nn, un))
