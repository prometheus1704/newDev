// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
 
contract BankAccount {
    // Owner address (the person who deploys the contract)
    address public owner;
 
    // Balance of the customer's bank account
    uint256 public balance;
 
    // Events to log transactions on the blockchain
    event Deposit(address indexed accountHolder, uint256 amount, uint256 newBalance);
    event Withdrawal(address indexed accountHolder, uint256 amount, uint256 newBalance);
 
    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // The deployer becomes the owner
        balance = 0; // Initial balance (you can set default if required)
    }
 
    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }
 
    // Function to deposit money into the account
    function deposit(uint256 amount) public onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        balance += amount;
        emit Deposit(msg.sender, amount, balance);
    }
 
    // Function to withdraw money from the account
    function withdraw(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(amount <= balance, "Insufficient balance");
        balance -= amount;
        emit Withdrawal(msg.sender, amount, balance);
    }
 
    // Function to check the current account balance
    function getBalance() public view returns (uint256) {
        return balance;
    }
 
    // Fallback function to handle incorrect calls
    fallback() external payable {
        revert("Invalid function call");
    }
 
    // Function to accept Ether (optional if you test with real ETH)
    receive() external payable {
        balance += msg.value;
        emit Deposit(msg.sender, msg.value, balance);
    }
}
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
 
// This **`BankAccount`** contract simulates a **personal bank account** on the blockchain.
 
// It allows the **owner (deployer)** to:
 
// - **Deposit** money (increase balance),
// - **Withdraw** money (decrease balance),
// - **Check** the current balance.
 
// It also **logs all deposits and withdrawals** publicly using **events**, and it includes safety checks like:
 
// - Only the **owner** can make deposits or withdrawals.
// - Prevents invalid function calls and zero-value transactions.
// ----------------------------------------------------------------------
 
// pragma solidity ^0.8.0; - 
 
// - This tells the compiler the **Solidity version** the code is compatible with.
// - `^0.8.0` means: use version **0.8.0 or higher**, but **below 0.9.0**.
// - Solidity 0.8.x versions include **automatic overflow and underflow protection**, which improves safety.
 
// - **Events** log data on the blockchain — they’re like “print statements,” but stored permanently in logs.
// - `indexed` means that this parameter can be used to **filter/search logs** easily.
// - These two events record:
//     - Who made the transaction (`accountHolder`)
//     - How much they deposited/withdrew (`amount`)
//     - The new balance after the operation (`newBalance`)
 
// **Constructor** runs **only once** — when the contract is first deployed.
 
// - `msg.sender` is the **address that deploys the contract**.
// - So the person who deploys becomes the **owner**.
// - The `balance` starts at `0` (you could set a default if needed).
 
// - **Modifiers** are reusable checks that can be applied to functions.
// - Here, it checks whether the **caller (`msg.sender`) is the owner**.
// - `require(condition, "error message")` ensures the condition is true; otherwise, it reverts the transaction with the message.
// - The `_` means “run the rest of the function after this check passes.”
 
// This function lets the **owner add money** to the account.
 
// - `uint256 amount` → amount to deposit.
// - `onlyOwner` → only the owner can call this.
// - `require(amount > 0)` → prevents zero or negative deposits.
// - `balance += amount;` → updates the balance.
// - `emit Deposit(...)` → logs the deposit on the blockchain.
 
// `view` → means it doesn’t modify the blockchain (read-only).
 
// - Returns the current balance.
// - It’s actually redundant since `balance` is already `public`, but it’s a clear method for checking.
 
// The **fallback function** is triggered when:
 
// - Someone calls a non-existent function, or
// - Sends data to the contract that doesn’t match any function signature.
 
// The **receive function** is a special built-in function to **accept Ether** directly.
 
// - It is called when someone sends Ether without calling any specific function.
 
