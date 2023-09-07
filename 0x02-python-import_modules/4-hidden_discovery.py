#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    nms = dir(hidden_4)
    for nm in nms:
        if nm[:2] != "__":
            print(nm)

