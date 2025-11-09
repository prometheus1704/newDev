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
