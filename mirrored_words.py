from collections import Counter
import pandas as pd
pd.set_option('display.max_rows', None)

qwerty_mirror = {
    'q':'p','w':'o','e':'i','r':'u','t':'y',
            's':'l','d':'k','f':'j','g':'h',
                    'c':'m','v':'n', 
                                    'b':'b',
    'p':'q','o':'w','i':'e','u':'r','y':'t',
            'l':'s','k':'d','j':'f','h':'g',
                    'm':'c','n':'v'}

for i in ['200','1k','5k','10k','25k','450k']:
    # Load a dictionary file of words
    with open(rf"wordlists\\english_{i}.txt") as f:
        words = set(w.strip().lower() for w in f if w.strip().isalpha())

    mirrorlist = [["",""]]

    for w in words:
        if (set(w) & set("azx")):
            continue
        mir_w = "".join(qwerty_mirror[l] for l in w)
        if (mir_w in words) and not(w in [x[1] for x in mirrorlist]):
            mirrorlist.append([w,mir_w])

    df_mirror = pd.DataFrame(sorted(mirrorlist,key=lambda pair:(len(pair[0]),pair[0])),columns=['word','mirror'])[1:]
    df_mirror.to_csv(f"results\\mirror_pairs_{i}.csv",index=False)

    print(f"\nUsing wordlist --> English_{i}.txt\n")
    print(f"\ttotal # pairs: {len(df_mirror)}\n")
    if len(df_mirror) > 0:
        longest = df_mirror['word'].str.len().max()
        df_longest = df_mirror[df_mirror['word'].str.len() == longest]
        print(f"\tlongest:{longest}\n\t{[[df_longest['word'].iloc[x],df_longest['mirror'].iloc[x]] for x in range(len(df_longest))]}")
