import { prisma } from "@/utils/db";
import { PrismaClient } from "@prisma/client";

export class baseRepo {
  protected readonly prisma: PrismaClient;

  constructor() {
    this.prisma = prisma;
  }
}
