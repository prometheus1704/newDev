#include <iostream>
#include <cuda_runtime.h>
#include <chrono>
#include <cmath>

#define TILE_SIZE 16

// CUDA kernel: each thread computes one element of C
__global__ void matrixMulCUDA(float *A, float *B, float *C, int M, int N, int K)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < M && col < K)
    {
        float sum = 0.0f;

        for (int i = 0; i < N; i++)
        {
            sum += A[row * N + i] * B[i * K + col];
        }

        C[row * K + col] = sum;
    }
}

// CPU serial matrix multiplication
void matrixMulCPU(float *A, float *B, float *C, int M, int N, int K)
{
    for (int row = 0; row < M; row++)
    {
        for (int col = 0; col < K; col++)
        {
            float sum = 0.0f;

            for (int i = 0; i < N; i++)
            {
                sum += A[row * N + i] * B[i * K + col];
            }

            C[row * K + col] = sum;
        }
    }
}

// Check CPU and GPU result
bool checkResult(float *cpu, float *gpu, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (fabs(cpu[i] - gpu[i]) > 1e-3)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    // Matrix dimensions:
    // A = M x N
    // B = N x K
    // C = M x K
    int M = 512;
    int N = 512;
    int K = 512;

    int sizeA = M * N;
    int sizeB = N * K;
    int sizeC = M * K;

    size_t bytesA = sizeA * sizeof(float);
    size_t bytesB = sizeB * sizeof(float);
    size_t bytesC = sizeC * sizeof(float);

    // Host memory
    float *h_A = new float[sizeA];
    float *h_B = new float[sizeB];
    float *h_C_cpu = new float[sizeC];
    float *h_C_gpu = new float[sizeC];

    // Initialize matrices
    for (int i = 0; i < sizeA; i++)
        h_A[i] = 1.0f;

    for (int i = 0; i < sizeB; i++)
        h_B[i] = 1.0f;

    // ---------------- CPU SERIAL MULTIPLICATION ----------------
    auto cpu_start = std::chrono::high_resolution_clock::now();

    matrixMulCPU(h_A, h_B, h_C_cpu, M, N, K);

    auto cpu_end = std::chrono::high_resolution_clock::now();

    double cpu_time = std::chrono::duration<double, std::milli>(cpu_end - cpu_start).count();

    // ---------------- CUDA PARALLEL MULTIPLICATION ----------------

    float *d_A, *d_B, *d_C;

    cudaMalloc(&d_A, bytesA);
    cudaMalloc(&d_B, bytesB);
    cudaMalloc(&d_C, bytesC);

    cudaMemcpy(d_A, h_A, bytesA, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, bytesB, cudaMemcpyHostToDevice);

    dim3 block(TILE_SIZE, TILE_SIZE);

    dim3 grid(
        (K + TILE_SIZE - 1) / TILE_SIZE,
        (M + TILE_SIZE - 1) / TILE_SIZE
    );

    cudaEvent_t gpu_start, gpu_end;
    cudaEventCreate(&gpu_start);
    cudaEventCreate(&gpu_end);

    cudaEventRecord(gpu_start);

    matrixMulCUDA<<<grid, block>>>(d_A, d_B, d_C, M, N, K);

    cudaEventRecord(gpu_end);
    cudaEventSynchronize(gpu_end);

    float gpu_time = 0.0f;
    cudaEventElapsedTime(&gpu_time, gpu_start, gpu_end);

    cudaMemcpy(h_C_gpu, d_C, bytesC, cudaMemcpyDeviceToHost);

    // ---------------- RESULT CHECK ----------------

    bool result = checkResult(h_C_cpu, h_C_gpu, sizeC);

    std::cout << "CPU Serial Time: " << cpu_time << " ms" << std::endl;
    std::cout << "CUDA Parallel Time: " << gpu_time << " ms" << std::endl;

    if (result)
        std::cout << "Result: PASS" << std::endl;
    else
        std::cout << "Result: FAIL" << std::endl;

    // Free memory
    delete[] h_A;
    delete[] h_B;
    delete[] h_C_cpu;
    delete[] h_C_gpu;

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    cudaEventDestroy(gpu_start);
    cudaEventDestroy(gpu_end);

    return 0;
}