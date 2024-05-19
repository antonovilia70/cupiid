def add_liq(
    self,
    pool_id: int,
    token_id: int,
    amount: int,
    max_amount: int = 0,
    min_amount: int = 0,
    deadline: int = 0,
) -> "TransactionReceipt":
    """
    Add liquidity to a pool.

    Args:
        pool_id: The ID of the pool to add liquidity to.
        token_id: The ID of the token to add liquidity for.
        amount: The amount of liquidity to add.
        max_amount: The maximum amount of liquidity to add.
            If the actual amount is greater than this value, the transaction will fail.
        min_amount: The minimum amount of liquidity to add.
            If the actual amount is less than this value, the transaction will fail.
        deadline: The deadline for the transaction.
            If the transaction is not completed by this deadline, it will fail.

    Returns:
        A transaction receipt.
    """

    return self.client.add_liquidity(
        pool_id=pool_id,
        token_id=token_id,
        amount=amount,
        max_amount=max_amount,
        min_amount=min_amount,
        deadline=deadline,
    )

