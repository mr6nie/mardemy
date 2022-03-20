def get_timer(length: float, type: str = "long"):
    h = length // 3600
    m = length % 3600 // 60
    s = length % 3600 % 60
    if type == "short":
        return f"{h}:{f'0{m}' if m < 10 else m}"

    if type == "min":
        return f"{f'{m}' if m < 10 else m}"

    else:
        if h >= 1:
            return (
                f"{h}:{f'{m}' if m < 10 else m}:{f'{round(s)}' if s < 10 else round(s)}"
            )
        else:
            return f"{f'{m}' if m < 10 else m}:{f'{round(s)}' if s < 10 else round(s)}"
